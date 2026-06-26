from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_SubscriptionsRead = Authenticator(
    required_scopes={
        Scope.subscriptions_read,
        Scope.subscriptions_write,
    },
    allowed_subjects={User, Organization},
)
SubscriptionsRead = Annotated[
    AuthSubject[User | Organization], Depends(_SubscriptionsRead)
]


_SubscriptionsWrite = Authenticator(
    required_scopes={
        Scope.subscriptions_write,
    },
    allowed_subjects={User, Organization},
)
SubscriptionsWrite = Annotated[
    AuthSubject[User | Organization], Depends(_SubscriptionsWrite)
]
