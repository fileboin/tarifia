from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_BenefitsRead = Authenticator(
    required_scopes={
        Scope.benefits_read,
        Scope.benefits_write,
    },
    allowed_subjects={User, Organization},
)
BenefitsRead = Annotated[AuthSubject[User | Organization], Depends(_BenefitsRead)]

_BenefitsWrite = Authenticator(
    required_scopes={
        Scope.benefits_write,
    },
    allowed_subjects={User, Organization},
)
BenefitsWrite = Annotated[AuthSubject[User | Organization], Depends(_BenefitsWrite)]
