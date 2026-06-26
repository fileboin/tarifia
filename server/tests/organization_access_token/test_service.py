from datetime import timedelta
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from tarifia.auth.models import AuthSubject
from tarifia.auth.scope import Scope
from tarifia.config import settings
from tarifia.email.schemas import OrganizationAccessTokenLeakedEmail
from tarifia.enums import TokenType
from tarifia.exceptions import TarifiaRequestValidationError
from tarifia.kit.crypto import get_token_hash
from tarifia.kit.utils import utc_now
from tarifia.models import (
    Organization,
    OrganizationAccessToken,
    PersonalAccessToken,
    User,
    UserOrganization,
)
from tarifia.organization_access_token.schemas import (
    AvailableScope,
    OrganizationAccessTokenCreate,
)
from tarifia.organization_access_token.service import (
    organization_access_token as organization_access_token_service,
)
from tarifia.postgres import AsyncSession
from tests.fixtures.database import SaveFixture


@pytest.fixture(autouse=True)
def enqueue_email_mock(mocker: MockerFixture) -> MagicMock:
    return mocker.patch(
        "tarifia.organization_access_token.service.enqueue_email_template",
        autospec=True,
    )


@pytest.mark.asyncio
class TestRevokeLeaked:
    async def test_false_positive(
        self, session: AsyncSession, enqueue_email_mock: MagicMock
    ) -> None:
        result = await organization_access_token_service.revoke_leaked(
            session,
            "tarifia_pat_123",
            TokenType.organization_access_token,
            notifier="github",
            url="https://github.com",
        )
        assert result is False

        enqueue_email_mock.assert_not_called()

    async def test_true_positive(
        self,
        save_fixture: SaveFixture,
        session: AsyncSession,
        organization: Organization,
        user_organization: UserOrganization,
        enqueue_email_mock: MagicMock,
    ) -> None:
        token_hash = get_token_hash("tarifia_pat_123", secret=settings.SECRET)
        organization_access_token = OrganizationAccessToken(
            comment="Test",
            token=token_hash,
            organization=organization,
            expires_at=utc_now() + timedelta(days=1),
            scope="openid",
        )
        await save_fixture(organization_access_token)

        result = await organization_access_token_service.revoke_leaked(
            session,
            "tarifia_pat_123",
            TokenType.organization_access_token,
            notifier="github",
            url="https://github.com",
        )
        assert result is True

        updated_organization_access_token = await session.get(
            OrganizationAccessToken, organization_access_token.id
        )
        assert updated_organization_access_token is not None
        assert updated_organization_access_token.deleted_at is not None

        enqueue_email_mock.assert_called_once()
        assert isinstance(
            enqueue_email_mock.call_args[0][0], OrganizationAccessTokenLeakedEmail
        )


@pytest.mark.asyncio
class TestCreateScopeValidation:
    async def test_pat_caller_cannot_mint_broader_scope(
        self,
        session: AsyncSession,
        user: User,
        organization: Organization,
        user_organization: UserOrganization,
    ) -> None:
        pat_session = MagicMock(spec=PersonalAccessToken)
        auth_subject: AuthSubject[User] = AuthSubject(
            user, {Scope.organization_access_tokens_write}, pat_session
        )

        with pytest.raises(TarifiaRequestValidationError):
            await organization_access_token_service.create(
                session,
                auth_subject,
                OrganizationAccessTokenCreate(
                    organization_id=organization.id,
                    comment="elevated",
                    scopes=[AvailableScope("orders:write")],
                ),
            )
