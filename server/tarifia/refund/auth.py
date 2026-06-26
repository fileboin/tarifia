from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

RefundsRead = Annotated[
    AuthSubject[User | Organization],
    Depends(
        Authenticator(
            required_scopes={
                Scope.refunds_read,
                Scope.refunds_write,
            },
            allowed_subjects={User, Organization},
        )
    ),
]

RefundsWrite = Annotated[
    AuthSubject[User | Organization],
    Depends(
        Authenticator(
            required_scopes={
                Scope.refunds_write,
            },
            allowed_subjects={User, Organization},
        )
    ),
]
