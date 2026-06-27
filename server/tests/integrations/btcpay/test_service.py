"""
Unit tests for the BTCPay service helper functions.
"""

from __future__ import annotations

import pytest

from polar.integrations.btcpay.service import _extract_payment_method


class TestExtractPaymentMethod:
    def test_lightning_from_payments_list(self) -> None:
        invoice = {
            "payments": [
                {"destination": "lnbc10u1p3jrpgqpp...", "amount": "0.000001"}
            ]
        }
        assert _extract_payment_method(invoice) == "bitcoin_lightning"

    def test_onchain_from_payments_list(self) -> None:
        invoice = {
            "payments": [
                {"destination": "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq", "amount": "0.001"}
            ]
        }
        assert _extract_payment_method(invoice) == "bitcoin_onchain"

    def test_lightning_from_payment_methods(self) -> None:
        invoice = {
            "payments": [],
            "paymentMethods": [
                {"paymentMethodId": "BTC_LightningNetwork", "amount": "0.0001"}
            ],
        }
        assert _extract_payment_method(invoice) == "bitcoin_lightning"

    def test_btc_onchain_from_payment_methods(self) -> None:
        invoice = {
            "payments": [],
            "paymentMethods": [
                {"paymentMethodId": "BTC", "amount": "0.001"}
            ],
        }
        assert _extract_payment_method(invoice) == "bitcoin_onchain"

    def test_fallback_to_bitcoin(self) -> None:
        assert _extract_payment_method({}) == "bitcoin"

    def test_evm_token(self) -> None:
        invoice = {
            "payments": [],
            "paymentMethods": [
                {"paymentMethodId": "ETH_USDT", "amount": "10.00"}
            ],
        }
        result = _extract_payment_method(invoice)
        assert result.startswith("evm_")
