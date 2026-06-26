from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_CustomFieldRead = Authenticator(
    required_scopes={
        Scope.custom_fields_read,
        Scope.custom_fields_write,
    },
    allowed_subjects={User, Organization},
)
CustomFieldRead = Annotated[AuthSubject[User | Organization], Depends(_CustomFieldRead)]

_CustomFieldWrite = Authenticator(
    required_scopes={
        Scope.custom_fields_write,
    },
    allowed_subjects={User, Organization},
)
CustomFieldWrite = Annotated[
    AuthSubject[User | Organization], Depends(_CustomFieldWrite)
]
