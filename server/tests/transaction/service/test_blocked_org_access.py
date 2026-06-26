import pytest

from tarifia.auth.models import AuthSubject
from tarifia.kit.pagination import PaginationParams
from tarifia.models import (
    Account,
    Organization,
    User,
    UserOrganization,
)
from tarifia.models.organization import OrganizationStatus
from tarifia.models.transaction import TransactionType
from tarifia.postgres import AsyncSession
from tarifia.transaction.service.transaction import transaction as transaction_service
from tests.fixtures.database import SaveFixture
from tests.transaction.conftest import create_transaction


@pytest.mark.asyncio
class TestBlockedOrganizationTransactionAccess:
    @pytest.mark.auth
    async def test_blocked_org_account_transactions_hidden(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User],
        save_fixture: SaveFixture,
        organization: Organization,
        user_organization: UserOrganization,
        account: Account,
    ) -> None:
        transaction = await create_transaction(
            save_fixture,
            type=TransactionType.balance,
            account=account,
        )

        organization.set_status(OrganizationStatus.BLOCKED)
        await save_fixture(organization)

        results, count = await transaction_service.search(
            session, auth_subject, pagination=PaginationParams(1, 10)
        )

        result_ids = [t.id for t in results]
        assert transaction.id not in result_ids
        assert count == 0

    @pytest.mark.auth
    async def test_blocked_org_payment_transactions_hidden(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User],
        save_fixture: SaveFixture,
        organization: Organization,
        user_organization: UserOrganization,
    ) -> None:
        transaction = await create_transaction(
            save_fixture,
            type=TransactionType.payment,
            payment_organization=organization,
        )

        organization.set_status(OrganizationStatus.BLOCKED)
        await save_fixture(organization)

        results, count = await transaction_service.search(
            session, auth_subject, pagination=PaginationParams(1, 10)
        )

        result_ids = [t.id for t in results]
        assert transaction.id not in result_ids
        assert count == 0

    @pytest.mark.auth
    async def test_direct_payment_transactions_visible_after_org_blocked(
        self,
        session: AsyncSession,
        auth_subject: AuthSubject[User],
        save_fixture: SaveFixture,
        user: User,
        organization: Organization,
        user_organization: UserOrganization,
    ) -> None:
        transaction = await create_transaction(
            save_fixture,
            type=TransactionType.payment,
            payment_user=user,
        )

        organization.set_status(OrganizationStatus.BLOCKED)
        await save_fixture(organization)

        results, count = await transaction_service.search(
            session, auth_subject, pagination=PaginationParams(1, 10)
        )

        result_ids = [t.id for t in results]
        assert transaction.id in result_ids
        assert count == 1
