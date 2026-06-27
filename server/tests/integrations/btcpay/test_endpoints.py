"""
Tests for the BTCPay Server webhook endpoint.

Covers:
- HMAC-SHA256 signature verification
- InvoiceSettled event dispatch
- InvoiceExpired / InvoiceInvalid event dispatch
- Invalid signature rejection
"""

from __future__ import annotations

import hashlib
import hmac
import json
from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient


def _sign(body: bytes, secret: str) -> str:
    return "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()


BASE_EVENT = {
    "deliveryId": "del_1",
    "webhookId": "wh_1",
    "originalDeliveryId": "del_1",
    "isRedelivery": False,
    "timestamp": 1700000000,
    "storeId": "store_1",
    "invoiceId": "inv_test123",
}

SETTLED_EVENT = {**BASE_EVENT, "type": "InvoiceSettled", "manuallyMarked": False, "overPaid": False}
EXPIRED_EVENT = {**BASE_EVENT, "type": "InvoiceExpired", "partiallyPaid": False}
INVALID_EVENT = {**BASE_EVENT, "type": "InvoiceInvalid", "manuallyMarked": False}


@pytest.mark.asyncio
class TestBTCPayWebhookSignature:
    @pytest.mark.parametrize("secret", ["my-webhook-secret", "another-secret-value"])
    async def test_valid_signature_accepted(
        self, secret: str, client: AsyncClient
    ) -> None:
        body = json.dumps(SETTLED_EVENT).encode()
        sig = _sign(body, secret)

        with (
            patch("polar.config.settings.BTCPAY_WEBHOOK_SECRET", secret),
            patch(
                "polar.integrations.btcpay.service.BTCPayService.handle_invoice_settled",
                new_callable=AsyncMock,
            ),
        ):
            response = await client.post(
                "/v1/integrations/btcpay/webhook",
                content=body,
                headers={"BTCPay-Sig": sig, "Content-Type": "application/json"},
            )
        assert response.status_code == 202

    async def test_invalid_signature_rejected(self, client: AsyncClient) -> None:
        body = json.dumps(SETTLED_EVENT).encode()

        with patch("polar.config.settings.BTCPAY_WEBHOOK_SECRET", "real-secret"):
            response = await client.post(
                "/v1/integrations/btcpay/webhook",
                content=body,
                headers={
                    "BTCPay-Sig": "sha256=deadbeef",
                    "Content-Type": "application/json",
                },
            )
        assert response.status_code == 401

    async def test_missing_signature_rejected(self, client: AsyncClient) -> None:
        body = json.dumps(SETTLED_EVENT).encode()

        with patch("polar.config.settings.BTCPAY_WEBHOOK_SECRET", "real-secret"):
            response = await client.post(
                "/v1/integrations/btcpay/webhook",
                content=body,
                headers={"Content-Type": "application/json"},
            )
        assert response.status_code == 401

    async def test_no_secret_configured_skips_verification(
        self, client: AsyncClient
    ) -> None:
        body = json.dumps(SETTLED_EVENT).encode()

        with (
            patch("polar.config.settings.BTCPAY_WEBHOOK_SECRET", ""),
            patch(
                "polar.integrations.btcpay.service.BTCPayService.handle_invoice_settled",
                new_callable=AsyncMock,
            ),
        ):
            response = await client.post(
                "/v1/integrations/btcpay/webhook",
                content=body,
                headers={"Content-Type": "application/json"},
            )
        assert response.status_code == 202


@pytest.mark.asyncio
class TestBTCPayWebhookEventDispatch:
    async def test_settled_event_calls_handle_settled(
        self, client: AsyncClient
    ) -> None:
        body = json.dumps(SETTLED_EVENT).encode()

        with (
            patch("polar.config.settings.BTCPAY_WEBHOOK_SECRET", ""),
            patch(
                "polar.integrations.btcpay.service.BTCPayService.handle_invoice_settled",
                new_callable=AsyncMock,
            ) as mock_settled,
        ):
            response = await client.post(
                "/v1/integrations/btcpay/webhook",
                content=body,
                headers={"Content-Type": "application/json"},
            )
        assert response.status_code == 202
        mock_settled.assert_called_once_with(
            pytest.approx(object()),  # session — any value
            "inv_test123",
        )

    async def test_expired_event_calls_handle_expired(
        self, client: AsyncClient
    ) -> None:
        body = json.dumps(EXPIRED_EVENT).encode()

        with (
            patch("polar.config.settings.BTCPAY_WEBHOOK_SECRET", ""),
            patch(
                "polar.integrations.btcpay.service.BTCPayService.handle_invoice_expired_or_invalid",
                new_callable=AsyncMock,
            ) as mock_expired,
        ):
            response = await client.post(
                "/v1/integrations/btcpay/webhook",
                content=body,
                headers={"Content-Type": "application/json"},
            )
        assert response.status_code == 202
        mock_expired.assert_called_once()
