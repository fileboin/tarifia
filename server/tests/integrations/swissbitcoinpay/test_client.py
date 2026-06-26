import json
from decimal import Decimal

import pytest
import respx

from polar.integrations.swissbitcoinpay.client import (
    SwissBitcoinPayAPIError,
    SwissBitcoinPayClient,
    SwissBitcoinPayConfigurationError,
)


@pytest.mark.asyncio
class TestCreateInvoice:
    @pytest.mark.respx(base_url="https://api.swiss-bitcoin-pay.ch")
    async def test_valid(self, respx_mock: respx.MockRouter) -> None:
        route = respx_mock.post("/checkout").respond(
            201,
            json={
                "id": "invoice_123",
                "checkoutUrl": "https://pay.swiss-bitcoin-pay.ch/invoice_123",
                "amount": 12.34,
            },
        )
        client = SwissBitcoinPayClient(
            api_key="sbp_test_key",
            api_url="https://api.swiss-bitcoin-pay.ch",
        )

        invoice = await client.create_invoice(
            amount=Decimal("12.34"),
            title="Polar",
            description="Polar - Product",
            unit="usd",
            redirect_after_paid="https://polar.sh/success",
            extra={"checkout_id": "checkout_123"},
        )

        assert invoice.id == "invoice_123"
        assert invoice.checkout_url == "https://pay.swiss-bitcoin-pay.ch/invoice_123"
        assert route.calls.last.request.headers["api-key"] == "sbp_test_key"
        assert route.calls.last.request.headers["content-type"] == "application/json"
        assert route.calls.last.request.content
        assert route.calls.last.request.url.path == "/checkout"
        assert json.loads(route.calls.last.request.content) == {
            "amount": 12.34,
            "title": "Polar",
            "description": "Polar - Product",
            "unit": "USD",
            "redirectAfterPaid": "https://polar.sh/success",
            "extra": {"checkout_id": "checkout_123"},
        }

    async def test_not_configured(self) -> None:
        client = SwissBitcoinPayClient(
            api_key=None,
            api_url="https://api.swiss-bitcoin-pay.ch",
        )

        with pytest.raises(SwissBitcoinPayConfigurationError):
            await client.create_invoice(
                amount=Decimal("12.34"),
                title="Polar",
                description="Polar - Product",
                unit="usd",
                redirect_after_paid="https://polar.sh/success",
                extra={"checkout_id": "checkout_123"},
            )

    @pytest.mark.respx(base_url="https://api.swiss-bitcoin-pay.ch")
    async def test_invalid_response(self, respx_mock: respx.MockRouter) -> None:
        respx_mock.post("/checkout").respond(201, json={"id": "invoice_123"})
        client = SwissBitcoinPayClient(
            api_key="sbp_test_key",
            api_url="https://api.swiss-bitcoin-pay.ch",
        )

        with pytest.raises(SwissBitcoinPayAPIError):
            await client.create_invoice(
                amount=Decimal("12.34"),
                title="Polar",
                description="Polar - Product",
                unit="usd",
                redirect_after_paid="https://polar.sh/success",
                extra={"checkout_id": "checkout_123"},
            )
