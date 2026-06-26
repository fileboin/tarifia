from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_EventRead = Authenticator(
    required_scopes={
        Scope.events_read,
        Scope.events_write,
    },
    allowed_subjects={User, Organization},
)
EventRead = Annotated[AuthSubject[User | Organization], Depends(_EventRead)]

_EventWrite = Authenticator(
    required_scopes={
        Scope.events_write,
    },
    allowed_subjects={User, Organization},
)
EventWrite = Annotated[AuthSubject[User | Organization], Depends(_EventWrite)]
