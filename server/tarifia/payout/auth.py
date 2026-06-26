from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope

_PayoutsRead = Authenticator(
    required_scopes={
        Scope.payouts_read,
    },
    allowed_subjects={User},
)
PayoutsRead = Annotated[AuthSubject[User], Depends(_PayoutsRead)]

_PayoutsWrite = Authenticator(
    required_scopes={
        Scope.payouts_write,
    },
    allowed_subjects={User},
)
PayoutsWrite = Annotated[AuthSubject[User], Depends(_PayoutsWrite)]
