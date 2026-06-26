from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_SlackIntegrationRead = Authenticator(
    required_scopes={Scope.organizations_read, Scope.organizations_write},
    allowed_subjects={User, Organization},
)
SlackIntegrationRead = Annotated[
    AuthSubject[User | Organization], Depends(_SlackIntegrationRead)
]

_SlackIntegrationWrite = Authenticator(
    required_scopes={Scope.organizations_write},
    allowed_subjects={User, Organization},
)
SlackIntegrationWrite = Annotated[
    AuthSubject[User | Organization], Depends(_SlackIntegrationWrite)
]
