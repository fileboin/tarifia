from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_MemberRead = Authenticator(
    required_scopes={
        Scope.members_read,
        Scope.members_write,
    },
    allowed_subjects={User, Organization},
)
MemberRead = Annotated[AuthSubject[User | Organization], Depends(_MemberRead)]

_MemberWrite = Authenticator(
    required_scopes={
        Scope.members_write,
    },
    allowed_subjects={User, Organization},
)
MemberWrite = Annotated[AuthSubject[User | Organization], Depends(_MemberWrite)]
