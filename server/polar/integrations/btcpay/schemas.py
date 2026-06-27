"""
Pydantic models for BTCPay Server webhook payloads.

Reference: https://docs.btcpayserver.org/API/Greenfield/v1/#tag/Webhooks
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel


class BTCPayWebhookBase(BaseModel):
    deliveryId: str
    webhookId: str
    originalDeliveryId: str
    isRedelivery: bool
    type: str
    timestamp: int
    storeId: str
    invoiceId: str


class BTCPayInvoiceSettled(BTCPayWebhookBase):
    type: Literal["InvoiceSettled"]
    manuallyMarked: bool = False
    overPaid: bool = False


class BTCPayInvoiceExpired(BTCPayWebhookBase):
    type: Literal["InvoiceExpired"]
    partiallyPaid: bool = False


class BTCPayInvoiceInvalid(BTCPayWebhookBase):
    type: Literal["InvoiceInvalid"]
    manuallyMarked: bool = False


# Any other webhook event we might receive but don't act on
class BTCPayInvoiceOther(BTCPayWebhookBase):
    pass


BTCPayWebhookEvent = (
    BTCPayInvoiceSettled | BTCPayInvoiceExpired | BTCPayInvoiceInvalid | BTCPayInvoiceOther
)


def parse_webhook_event(data: dict[str, Any]) -> BTCPayWebhookEvent:
    event_type = data.get("type", "")
    if event_type == "InvoiceSettled":
        return BTCPayInvoiceSettled(**data)
    if event_type == "InvoiceExpired":
        return BTCPayInvoiceExpired(**data)
    if event_type == "InvoiceInvalid":
        return BTCPayInvoiceInvalid(**data)
    return BTCPayInvoiceOther(**data)
