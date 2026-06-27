from decimal import Decimal
from typing import Any

import httpx

from polar.config import settings
from polar.exceptions import PolarError


class SwissBitcoinPayError(PolarError): ...


class SwissBitcoinPayConfigurationError(SwissBitcoinPayError):
    def __init__(self) -> None:
        super().__init__("Swiss Bitcoin Pay is not configured.", 503)


class SwissBitcoinPayAPIError(SwissBitcoinPayError):
    def __init__(self, message: str = "Unable to create crypto payment.") -> None:
        super().__init__(message, 502)


class SwissBitcoinPayInvoice:
    def __init__(self, *, id: str, checkout_url: str) -> None:
        self.id = id
        self.checkout_url = checkout_url


class SwissBitcoinPayClient:
    def __init__(self, *, api_key: str | None, api_url: str) -> None:
        self._api_key = api_key
        self._client = httpx.AsyncClient(
            base_url=api_url,
            headers={"api-key": api_key} if api_key else {},
            timeout=httpx.Timeout(10.0, connect=5.0),
        )

    async def create_invoice(
        self,
        *,
        amount: Decimal,
        title: str,
        description: str,
        unit: str,
        redirect_after_paid: str,
        extra: dict[str, Any],
    ) -> SwissBitcoinPayInvoice:
        if not self._api_key:
            raise SwissBitcoinPayConfigurationError()

        try:
            response = await self._client.post(
                "/checkout",
                json={
                    "amount": float(amount),
                    "title": title,
                    "description": description,
                    "unit": unit.upper(),
                    "redirectAfterPaid": redirect_after_paid,
                    "extra": extra,
                },
            )
        except httpx.RequestError as e:
            raise SwissBitcoinPayAPIError() from e

        if response.status_code != 201:
            raise SwissBitcoinPayAPIError()

        try:
            data = response.json()
            invoice_id = data["id"]
            checkout_url = data["checkoutUrl"]
        except (KeyError, ValueError, TypeError) as e:
            raise SwissBitcoinPayAPIError(
                "Invalid response from Swiss Bitcoin Pay."
            ) from e

        return SwissBitcoinPayInvoice(id=invoice_id, checkout_url=checkout_url)


def get_swissbitcoinpay_client() -> SwissBitcoinPayClient:
    return SwissBitcoinPayClient(
        api_key=settings.SWISS_BITCOIN_PAY_API_KEY,
        api_url=settings.SWISS_BITCOIN_PAY_API_URL,
    )
