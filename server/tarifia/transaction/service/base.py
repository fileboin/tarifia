import itertools

from sqlalchemy import select

from tarifia.exceptions import TarifiaError
from tarifia.kit.services import ResourceServiceReader
from tarifia.models import Transaction
from tarifia.models.transaction import TransactionType
from tarifia.postgres import AsyncSession


class BaseTransactionServiceError(TarifiaError): ...


class BaseTransactionService(ResourceServiceReader[Transaction]):
    async def _get_balance_transactions_for_payment(
        self, session: AsyncSession, *, payment_transaction: Transaction
    ) -> list[tuple[Transaction, Transaction]]:
        statement = (
            select(Transaction)
            .where(
                Transaction.type == TransactionType.balance,
                Transaction.payment_transaction_id == payment_transaction.id,
            )
            .order_by(
                Transaction.balance_correlation_key,
                Transaction.account_id.nulls_first(),
            )
        )

        result = await session.execute(statement)
        transactions = list(result.scalars().all())
        return [
            (t1, t2)
            for _, (t1, t2) in itertools.groupby(
                transactions, key=lambda t: t.balance_correlation_key
            )
        ]
