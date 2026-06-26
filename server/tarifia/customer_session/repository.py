from uuid import UUID

from sqlalchemy import delete

from tarifia.kit.repository import RepositoryBase
from tarifia.kit.utils import utc_now
from tarifia.models import CustomerSession


class CustomerSessionRepository(RepositoryBase[CustomerSession]):
    model = CustomerSession

    async def delete_by_customer_id(self, customer_id: UUID) -> None:
        statement = delete(CustomerSession).where(
            CustomerSession.customer_id == customer_id
        )
        await self.session.execute(statement)

    async def delete_expired(self) -> None:
        statement = delete(CustomerSession).where(
            CustomerSession.expires_at < utc_now()
        )
        await self.session.execute(statement)
