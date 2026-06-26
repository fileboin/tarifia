from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_CreatorProductsRead = Authenticator(
    required_scopes={
        Scope.products_read,
        Scope.products_write,
    },
    allowed_subjects={User, Organization},
)
CreatorProductsRead = Annotated[
    AuthSubject[User | Organization], Depends(_CreatorProductsRead)
]

_CreatorProductsWrite = Authenticator(
    required_scopes={
        Scope.products_write,
    },
    allowed_subjects={User, Organization},
)
CreatorProductsWrite = Annotated[
    AuthSubject[User | Organization], Depends(_CreatorProductsWrite)
]
