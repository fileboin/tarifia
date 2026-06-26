from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_EventTypeRead = Authenticator(
    required_scopes={
        Scope.events_read,
        Scope.events_write,
    },
    allowed_subjects={User, Organization},
)
EventTypeRead = Annotated[AuthSubject[User | Organization], Depends(_EventTypeRead)]

_EventTypeWrite = Authenticator(
    required_scopes={Scope.events_write},
    allowed_subjects={User, Organization},
)
EventTypeWrite = Annotated[AuthSubject[User | Organization], Depends(_EventTypeWrite)]
