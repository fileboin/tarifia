from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_CustomerRead = Authenticator(
    required_scopes={
        Scope.customers_read,
        Scope.customers_write,
    },
    allowed_subjects={User, Organization},
)
CustomerRead = Annotated[AuthSubject[User | Organization], Depends(_CustomerRead)]

_CustomerWrite = Authenticator(
    required_scopes={
        Scope.customers_write,
    },
    allowed_subjects={User, Organization},
)
CustomerWrite = Annotated[AuthSubject[User | Organization], Depends(_CustomerWrite)]
