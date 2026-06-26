from decimal import Decimal

from polar.exceptions import PolarError
from polar.integrations.swissbitcoinpay.client import SwissBitcoinPayClient
from polar.kit.currency import get_currency_decimal_factor
from polar.models import Checkout
from polar.models.checkout import CheckoutStatus


class CheckoutCryptoPaymentError(PolarError): ...


class CryptoPaymentNotSupported(CheckoutCryptoPaymentError):
    def __init__(self, message: str = "Crypto payment is not supported.") -> None:
        super().__init__(message, 403)


class CryptoPaymentURL:
    def __init__(self, *, payment_url: str) -> None:
        self.payment_url = payment_url


class CheckoutCryptoService:
    async def create_payment_url(
        self, checkout: Checkout, client: SwissBitcoinPayClient
    ) -> CryptoPaymentURL:
        if checkout.status != CheckoutStatus.open:
            raise CryptoPaymentNotSupported("Checkout is not open.")

        if checkout.is_expired:
            raise CryptoPaymentNotSupported("Checkout has expired.")

        if not checkout.is_payment_required:
            raise CryptoPaymentNotSupported("Checkout does not require a payment.")

        if checkout.should_save_payment_method:
            raise CryptoPaymentNotSupported(
                "Crypto payment is only supported for one-time checkouts."
            )

        amount = Decimal(checkout.total_amount) / Decimal(
            get_currency_decimal_factor(checkout.currency)
        )
        invoice = await client.create_invoice(
            amount=amount,
            title=checkout.organization.name,
            description=checkout.description,
            unit=checkout.currency,
            redirect_after_paid=checkout.success_url,
            extra={"checkout_id": str(checkout.id)},
        )

        checkout.payment_processor_metadata = {
            **checkout.payment_processor_metadata,
            "swissbitcoinpay_invoice_id": invoice.id,
        }

        return CryptoPaymentURL(payment_url=invoice.checkout_url)


checkout_crypto = CheckoutCryptoService()
