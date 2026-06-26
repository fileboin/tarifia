from typing import Protocol

from pydantic import UUID4

from tarifia.auth.models import AuthSubject, is_organization
from tarifia.authz.service import get_accessible_org_ids
from tarifia.exceptions import TarifiaRequestValidationError
from tarifia.models import Organization, User
from tarifia.organization.repository import OrganizationRepository
from tarifia.postgres import AsyncSession


class _OrganizationIDModelNone(Protocol):
    organization_id: UUID4 | None


class _OrganizationIDModel(Protocol):
    organization_id: UUID4


OrganizationIDModel = _OrganizationIDModelNone | _OrganizationIDModel


async def get_payload_organization(
    session: AsyncSession,
    auth_subject: AuthSubject[User | Organization],
    model: OrganizationIDModel,
) -> Organization:
    if is_organization(auth_subject):
        if model.organization_id is not None:
            raise TarifiaRequestValidationError(
                [
                    {
                        "type": "organization_token",
                        "msg": (
                            "Setting organization_id is disallowed "
                            "when using an organization token."
                        ),
                        "loc": (
                            "body",
                            "organization_id",
                        ),
                        "input": model.organization_id,
                    }
                ]
            )
        return auth_subject.subject

    repository = OrganizationRepository.from_session(session)

    if model.organization_id is None:
        # A credential down-scoped to exactly one organization resolves it
        # implicitly, restoring organization-token ergonomics on create
        # endpoints.
        if (
            auth_subject.organization_ids is not None
            and len(auth_subject.organization_ids) == 1
        ):
            accessible = await get_accessible_org_ids(session, auth_subject)
            if len(accessible) == 1:
                organization = await repository.get_by_id(next(iter(accessible)))
                if organization is not None:
                    return organization
        raise TarifiaRequestValidationError(
            [
                {
                    "type": "missing",
                    "msg": "organization_id is required.",
                    "loc": (
                        "body",
                        "organization_id",
                    ),
                    "input": None,
                }
            ]
        )

    accessible = await get_accessible_org_ids(session, auth_subject)
    if model.organization_id not in accessible:
        raise TarifiaRequestValidationError(
            [
                {
                    "loc": (
                        "body",
                        "organization_id",
                    ),
                    "msg": "Organization not found.",
                    "type": "value_error",
                    "input": model.organization_id,
                }
            ]
        )

    organization = await repository.get_by_id(model.organization_id)

    if organization is None:
        raise TarifiaRequestValidationError(
            [
                {
                    "loc": (
                        "body",
                        "organization_id",
                    ),
                    "msg": "Organization not found.",
                    "type": "value_error",
                    "input": model.organization_id,
                }
            ]
        )

    return organization
