from fastapi import Depends
from pydantic import UUID4

from tarifia.authz.dependencies import AuthorizeWebUserRead, AuthorizeWebUserWrite
from tarifia.exceptions import ResourceNotFound
from tarifia.kit.pagination import ListResource, PaginationParamsQuery
from tarifia.openapi import APITag
from tarifia.postgres import AsyncSession, get_db_session
from tarifia.routing import APIRouter

from .schemas import PersonalAccessToken
from .service import personal_access_token as personal_access_token_service

router = APIRouter(
    prefix="/personal_access_tokens", tags=["personal_access_token", APITag.private]
)


@router.get("/", response_model=ListResource[PersonalAccessToken])
async def list_personal_access_tokens(
    auth_subject: AuthorizeWebUserRead,
    pagination: PaginationParamsQuery,
    session: AsyncSession = Depends(get_db_session),
) -> ListResource[PersonalAccessToken]:
    """List personal access tokens."""
    results, count = await personal_access_token_service.list(
        session, auth_subject, pagination=pagination
    )

    return ListResource.from_paginated_results(
        [PersonalAccessToken.model_validate(result) for result in results],
        count,
        pagination,
    )


@router.delete("/{id}", status_code=204)
async def delete_personal_access_token(
    id: UUID4,
    auth_subject: AuthorizeWebUserWrite,
    session: AsyncSession = Depends(get_db_session),
) -> None:
    personal_access_token = await personal_access_token_service.get_by_id(
        session, auth_subject, id
    )
    if personal_access_token is None:
        raise ResourceNotFound()

    await personal_access_token_service.delete(session, personal_access_token)
