from typing import Annotated

from fastapi import Depends

from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.authz.dependencies import WebUserAuthorizer

_OrganizationAccessTokensRead = WebUserAuthorizer(
    required_scopes={
        Scope.organization_access_tokens_read,
        Scope.organization_access_tokens_write,
    }
)
OrganizationAccessTokensRead = Annotated[
    AuthSubject[User], Depends(_OrganizationAccessTokensRead)
]

_OrganizationAccessTokensWrite = WebUserAuthorizer(
    required_scopes={
        Scope.organization_access_tokens_write,
    }
)
OrganizationAccessTokensWrite = Annotated[
    AuthSubject[User], Depends(_OrganizationAccessTokensWrite)
]
