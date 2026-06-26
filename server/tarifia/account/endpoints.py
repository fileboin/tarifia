from fastapi import Depends

from tarifia.account_credit.repository import AccountCreditRepository
from tarifia.account_credit.schemas import AccountCredit as AccountCreditSchema
from tarifia.authz.dependencies import AuthorizeAccountRead, AuthorizeAccountWrite
from tarifia.models import Account
from tarifia.openapi import APITag
from tarifia.postgres import (
    AsyncReadSession,
    AsyncSession,
    get_db_read_session,
    get_db_session,
)
from tarifia.routing import APIRouter

from .schemas import Account as AccountSchema
from .schemas import AccountUpdate
from .service import account as account_service

router = APIRouter(tags=["accounts", APITag.private])


@router.get("/accounts/{id}", response_model=AccountSchema)
async def get(
    authz: AuthorizeAccountRead,
) -> Account:
    return authz.account


@router.patch("/accounts/{id}", response_model=AccountSchema)
async def patch(
    authz: AuthorizeAccountWrite,
    account_update: AccountUpdate,
    session: AsyncSession = Depends(get_db_session),
) -> Account:
    return await account_service.update(session, authz.account, account_update)


@router.get("/accounts/{id}/credits", response_model=list[AccountCreditSchema])
async def get_credits(
    authz: AuthorizeAccountRead,
    session: AsyncReadSession = Depends(get_db_read_session),
) -> list[AccountCreditSchema]:
    credit_repository = AccountCreditRepository.from_session(session)
    credits = await credit_repository.get_active(authz.account.id)
    return [AccountCreditSchema.model_validate(credit) for credit in credits]
