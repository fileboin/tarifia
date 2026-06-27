"""
BTCPay Server webhook endpoint.

BTCPay signs each delivery with an HMAC-SHA256 digest of the raw request body,
sent in the ``BTCPay-Sig`` header as ``sha256=<hex>``.  We verify the signature
before processing any event.
"""

from __future__ import annotations

import hashlib
import hmac

import structlog
from fastapi import Depends, HTTPException, Request

from polar.config import settings
from polar.logging import Logger
from polar.postgres import AsyncSession, get_db_session
from polar.routing import APIRouter

from .schemas import (
    BTCPayInvoiceExpired,
    BTCPayInvoiceInvalid,
    BTCPayInvoiceSettled,
    parse_webhook_event,
)
from .service import btcpay as btcpay_service

log: Logger = structlog.get_logger()

router = APIRouter(
    prefix="/integrations/btcpay",
    tags=["integrations_btcpay"],
    include_in_schema=False,
)

_SIG_HEADER = "BTCPay-Sig"


def _verify_signature(body: bytes, sig_header: str | None) -> bool:
    # If no secret is configured, skip verification (development mode)
    if not settings.BTCPAY_WEBHOOK_SECRET:
        return True

    if sig_header is None:
        return False

    digest = hmac.new(
        settings.BTCPAY_WEBHOOK_SECRET.encode(), body, hashlib.sha256
    ).hexdigest()
    expected = f"sha256={digest}"
    return hmac.compare_digest(expected, sig_header)


@router.post("/webhook", status_code=202, name="integrations.btcpay.webhook")
async def btcpay_webhook(
    request: Request,
    session: AsyncSession = Depends(get_db_session),
) -> None:
    body = await request.body()
    sig_header = request.headers.get(_SIG_HEADER)

    if not _verify_signature(body, sig_header):
        log.warning("btcpay.webhook_invalid_signature", sig=sig_header)
        raise HTTPException(status_code=401, detail="Invalid webhook signature")

    try:
        data = await request.json()
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Invalid JSON payload") from exc

    event = parse_webhook_event(data)
    invoice_id: str = event.invoiceId

    log.info("btcpay.webhook_received", type=event.type, invoice_id=invoice_id)

    if isinstance(event, BTCPayInvoiceSettled):
        await btcpay_service.handle_invoice_settled(session, invoice_id)

    elif isinstance(event, (BTCPayInvoiceExpired, BTCPayInvoiceInvalid)):
        await btcpay_service.handle_invoice_expired_or_invalid(session, invoice_id)
