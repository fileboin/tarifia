from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_WebhooksRead = Authenticator(
    required_scopes={
        Scope.webhooks_read,
        Scope.webhooks_write,
    },
    allowed_subjects={User, Organization},
)
WebhooksRead = Annotated[AuthSubject[User | Organization], Depends(_WebhooksRead)]

_WebhooksWrite = Authenticator(
    required_scopes={
        Scope.webhooks_write,
    },
    allowed_subjects={User, Organization},
)
WebhooksWrite = Annotated[AuthSubject[User | Organization], Depends(_WebhooksWrite)]
