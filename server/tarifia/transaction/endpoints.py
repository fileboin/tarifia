from typing import Annotated

from fastapi import Depends, Query
from pydantic import UUID4

from tarifia.account.service import account as account_service
from tarifia.auth.permission import OrganizationPermission
from tarifia.exceptions import ResourceNotFound
from tarifia.kit.pagination import ListResource, PaginationParamsQuery
from tarifia.kit.sorting import Sorting, SortingGetter
from tarifia.models.transaction import TransactionType
from tarifia.openapi import APITag
from tarifia.postgres import AsyncReadSession, get_db_read_session
from tarifia.routing import APIRouter
from tarifia.transaction import (
    auth as transactions_auth,
)

from .schemas import Transaction, TransactionsSummary
from .service.transaction import TransactionSortProperty
from .service.transaction import transaction as transaction_service

router = APIRouter(prefix="/transactions", tags=["transactions", APITag.private])


SearchSorting = Annotated[
    list[Sorting[TransactionSortProperty]],
    Depends(SortingGetter(TransactionSortProperty, ["-created_at"])),
]


@router.get("/search", response_model=ListResource[Transaction])
async def search_transactions(
    pagination: PaginationParamsQuery,
    sorting: SearchSorting,
    auth_subject: transactions_auth.TransactionsRead,
    type: TransactionType | None = Query(None),
    account_id: UUID4 | None = Query(None),
    payment_customer_id: UUID4 | None = Query(None),
    payment_organization_id: UUID4 | None = Query(None),
    payment_user_id: UUID4 | None = Query(None),
    exclude_platform_fees: bool = Query(False),
    session: AsyncReadSession = Depends(get_db_read_session),
) -> ListResource[Transaction]:
    results, count = await transaction_service.search(
        session,
        auth_subject,
        type=type,
        account_id=account_id,
        payment_customer_id=payment_customer_id,
        payment_organization_id=payment_organization_id,
        payment_user_id=payment_user_id,
        exclude_platform_fees=exclude_platform_fees,
        pagination=pagination,
        sorting=sorting,
    )

    return ListResource.from_paginated_results(
        [Transaction.model_validate(result) for result in results],
        count,
        pagination,
    )


@router.get("/summary", response_model=TransactionsSummary)
async def get_summary(
    auth_subject: transactions_auth.TransactionsRead,
    account_id: UUID4,
    session: AsyncReadSession = Depends(get_db_read_session),
) -> TransactionsSummary:
    account = await account_service.get(
        session,
        auth_subject,
        account_id,
        permission=OrganizationPermission.finance_read,
    )
    if account is None:
        raise ResourceNotFound()

    return await transaction_service.get_summary(session, account)
