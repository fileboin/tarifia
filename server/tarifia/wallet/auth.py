from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_WalletsRead = Authenticator(
    required_scopes={Scope.wallets_read},
    allowed_subjects={User, Organization},
)
WalletsRead = Annotated[AuthSubject[User | Organization], Depends(_WalletsRead)]

_WalletsWrite = Authenticator(
    required_scopes={
        Scope.wallets_write,
    },
    allowed_subjects={User, Organization},
)
WalletsWrite = Annotated[AuthSubject[User | Organization], Depends(_WalletsWrite)]
