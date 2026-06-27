"""
BTCPay Server service — bridge between the Polar checkout flow and the BTCPay
REST API.
"""

from __future__ import annotations

import uuid
from decimal import Decimal

import structlog

from polar.checkout.repository import CheckoutRepository
from polar.checkout.service import checkout as checkout_service
from polar.config import settings
from polar.enums import PaymentProcessor
from polar.kit.utils import generate_uuid
from polar.logging import Logger
from polar.models import Checkout, Payment
from polar.models.checkout import CheckoutStatus
from polar.models.payment import PaymentStatus, PaymentTrigger
from polar.payment.repository import PaymentRepository
from polar.postgres import AsyncSession

from . import client as btcpay_client
from .client import BTCPayError

log: Logger = structlog.get_logger()

# BTCPay metadata key we use to store our checkout id inside the invoice
BTCPAY_METADATA_CHECKOUT_ID = "polar_checkout_id"
BTCPAY_METADATA_ORGANIZATION_ID = "polar_organization_id"


class BTCPayServiceError(Exception):
    pass


class BTCPayService:
    async def create_invoice_for_checkout(
        self,
        session: AsyncSession,
        checkout: Checkout,
    ) -> str:
        """
        Create a BTCPay invoice for *checkout* and store the invoice id + url in
        ``checkout.payment_processor_metadata``.

        Returns the BTCPay-hosted checkout URL to which the customer should be
        redirected.
        """
        # Convert from smallest currency unit (cents) to decimal string expected
        # by BTCPay (e.g. 1000 USD cents → "10.00")
        amount_decimal = Decimal(checkout.total_amount) / Decimal(100)
        amount_str = f"{amount_decimal:.2f}"

        redirect_url = settings.generate_frontend_url(
            f"/checkout/{checkout.client_secret}/confirmation"
        )

        metadata: dict[str, str] = {
            BTCPAY_METADATA_CHECKOUT_ID: str(checkout.id),
            BTCPAY_METADATA_ORGANIZATION_ID: str(checkout.organization_id),
        }
        if checkout.customer_email:
            metadata["buyerEmail"] = checkout.customer_email

        try:
            invoice = await btcpay_client.create_invoice(
                amount=amount_str,
                currency=checkout.currency.upper(),
                metadata=metadata,
                redirect_url=redirect_url,
                checkout_description=checkout.description,
            )
        except BTCPayError as e:
            log.error(
                "btcpay.create_invoice_failed",
                checkout_id=str(checkout.id),
                error=str(e),
            )
            raise BTCPayServiceError(str(e)) from e

        invoice_id: str = invoice["id"]
        invoice_url: str = invoice["checkoutLink"]

        checkout.payment_processor_metadata = {
            **(checkout.payment_processor_metadata or {}),
            "btcpay_invoice_id": invoice_id,
            "btcpay_invoice_url": invoice_url,
        }
        session.add(checkout)

        log.info(
            "btcpay.invoice_created",
            checkout_id=str(checkout.id),
            invoice_id=invoice_id,
        )
        return invoice_url

    async def handle_invoice_settled(
        self,
        session: AsyncSession,
        invoice_id: str,
    ) -> None:
        """
        Called when BTCPay fires an ``InvoiceSettled`` webhook.  Looks up the
        associated checkout by the invoice id stored in metadata, creates a
        Payment record, and delegates to ``checkout_service.handle_success``.
        """
        repository = CheckoutRepository.from_session(session)

        checkout = await repository.get_by_btcpay_invoice_id(invoice_id)
        if checkout is None:
            log.warning(
                "btcpay.settled_invoice_no_checkout",
                invoice_id=invoice_id,
            )
            return

        if checkout.status != CheckoutStatus.confirmed:
            log.warning(
                "btcpay.settled_invoice_checkout_not_confirmed",
                invoice_id=invoice_id,
                checkout_id=str(checkout.id),
                checkout_status=checkout.status,
            )
            return

        # Fetch the invoice to get payment method details
        try:
            invoice_data = await btcpay_client.get_invoice(invoice_id)
        except BTCPayError as e:
            log.error(
                "btcpay.get_invoice_failed",
                invoice_id=invoice_id,
                error=str(e),
            )
            raise

        payment_method_name = _extract_payment_method(invoice_data)

        payment = await self._upsert_payment(
            session,
            checkout=checkout,
            invoice_id=invoice_id,
            invoice_data=invoice_data,
            payment_method_name=payment_method_name,
            status=PaymentStatus.succeeded,
        )

        await checkout_service.handle_success(session, checkout, payment=payment)

        log.info(
            "btcpay.checkout_succeeded",
            checkout_id=str(checkout.id),
            invoice_id=invoice_id,
        )

    async def handle_invoice_expired_or_invalid(
        self,
        session: AsyncSession,
        invoice_id: str,
    ) -> None:
        """
        Called when BTCPay fires ``InvoiceExpired`` or ``InvoiceInvalid``.
        Records a failed payment and triggers checkout failure handling.
        """
        repository = CheckoutRepository.from_session(session)
        checkout = await repository.get_by_btcpay_invoice_id(invoice_id)
        if checkout is None:
            return

        if checkout.status not in (
            CheckoutStatus.confirmed,
            CheckoutStatus.open,
        ):
            return

        try:
            invoice_data = await btcpay_client.get_invoice(invoice_id)
        except BTCPayError:
            invoice_data = {}

        payment_method_name = _extract_payment_method(invoice_data) or "bitcoin"

        payment = await self._upsert_payment(
            session,
            checkout=checkout,
            invoice_id=invoice_id,
            invoice_data=invoice_data,
            payment_method_name=payment_method_name,
            status=PaymentStatus.failed,
        )

        await checkout_service.handle_failure(session, checkout, payment=payment)

    async def _upsert_payment(
        self,
        session: AsyncSession,
        *,
        checkout: Checkout,
        invoice_id: str,
        invoice_data: dict,
        payment_method_name: str,
        status: PaymentStatus,
    ) -> Payment:
        payment_repository = PaymentRepository.from_session(session)

        payment = await payment_repository.get_by_processor_id(
            PaymentProcessor.btcpay, invoice_id
        )
        if payment is None:
            payment = Payment(
                id=generate_uuid(),
                processor=PaymentProcessor.btcpay,
                processor_id=invoice_id,
            )

        payment.status = status
        payment.amount = checkout.total_amount
        payment.currency = checkout.currency
        payment.method = payment_method_name
        payment.method_metadata = {
            "invoice_id": invoice_id,
            "btcpay_status": invoice_data.get("status", ""),
        }
        payment.customer_email = checkout.customer_email
        payment.trigger = PaymentTrigger.purchase
        payment.checkout = checkout
        payment.organization = checkout.organization

        return await payment_repository.update(payment)


def _extract_payment_method(invoice_data: dict) -> str:
    """
    Derive a human-readable payment method string from BTCPay invoice data.

    BTCPay returns the payment method used via the ``paymentMethods`` list or
    the ``payments`` list.  We fall back to "bitcoin" when neither is present.
    """
    payments: list[dict] = invoice_data.get("payments", [])
    if payments:
        dest = payments[0].get("destination", "")
        if dest.startswith("ln") or dest.startswith("lnbc"):
            return "bitcoin_lightning"
        return "bitcoin_onchain"

    # Inspect paymentMethods for the first settled one
    payment_methods: list[dict] = invoice_data.get("paymentMethods", [])
    for pm in payment_methods:
        if pm.get("amount", "0") != "0":
            raw = pm.get("paymentMethodId", "BTC").upper()
            if "LIGHTNING" in raw or "LN" in raw:
                return "bitcoin_lightning"
            if raw.startswith("ETH") or "_" in raw:
                return f"evm_{raw.lower()}"
            return "bitcoin_onchain"

    return "bitcoin"


btcpay = BTCPayService()
