from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_CustomerSessionWrite = Authenticator(
    required_scopes={
        Scope.customer_sessions_write,
    },
    allowed_subjects={User, Organization},
)
CustomerSessionWrite = Annotated[
    AuthSubject[User | Organization], Depends(_CustomerSessionWrite)
]
