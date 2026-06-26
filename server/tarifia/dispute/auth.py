from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_DisputesRead = Authenticator(
    required_scopes={Scope.disputes_read},
    allowed_subjects={User, Organization},
)
DisputesRead = Annotated[AuthSubject[User | Organization], Depends(_DisputesRead)]
