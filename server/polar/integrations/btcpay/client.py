"""
Low-level BTCPay Server REST API client.

All amounts are in the presentment currency (e.g. USD cents converted to USD
decimal strings by the service layer before calling here).
"""

from __future__ import annotations

from typing import Any

import httpx
import structlog

from polar.config import settings
from polar.logging import Logger

log: Logger = structlog.get_logger()


class BTCPayError(Exception):
    def __init__(self, status_code: int, detail: str) -> None:
        self.status_code = status_code
        super().__init__(f"BTCPay API error {status_code}: {detail}")


def _client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        base_url=settings.BTCPAY_URL.rstrip("/"),
        headers={
            "Authorization": f"token {settings.BTCPAY_API_KEY}",
            "Content-Type": "application/json",
        },
        timeout=15.0,
    )


async def create_invoice(
    *,
    amount: str,
    currency: str,
    metadata: dict[str, str],
    redirect_url: str,
    checkout_description: str | None = None,
) -> dict[str, Any]:
    """Create a BTCPay invoice and return the raw response dict."""
    payload: dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "metadata": metadata,
        "checkout": {
            "redirectURL": redirect_url,
            # MediumSpeed = 1 confirmation for on-chain, instant for Lightning
            "speedPolicy": "MediumSpeed",
        },
    }
    if checkout_description:
        payload["additionalData"] = {"description": checkout_description}

    async with _client() as client:
        resp = await client.post(
            f"/api/v1/stores/{settings.BTCPAY_STORE_ID}/invoices",
            json=payload,
        )

    if not resp.is_success:
        raise BTCPayError(resp.status_code, resp.text)

    return resp.json()


async def get_invoice(invoice_id: str) -> dict[str, Any]:
    async with _client() as client:
        resp = await client.get(
            f"/api/v1/stores/{settings.BTCPAY_STORE_ID}/invoices/{invoice_id}"
        )

    if not resp.is_success:
        raise BTCPayError(resp.status_code, resp.text)

    return resp.json()
