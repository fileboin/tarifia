from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_MeterRead = Authenticator(
    required_scopes={
        Scope.meters_read,
        Scope.meters_write,
    },
    allowed_subjects={User, Organization},
)
MeterRead = Annotated[AuthSubject[User | Organization], Depends(_MeterRead)]

_MeterWrite = Authenticator(
    required_scopes={
        Scope.meters_write,
    },
    allowed_subjects={User, Organization},
)
MeterWrite = Annotated[AuthSubject[User | Organization], Depends(_MeterWrite)]
