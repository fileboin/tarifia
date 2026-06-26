from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope

_SearchRead = Authenticator(
    required_scopes={
        Scope.products_read,
        Scope.products_write,
        Scope.customers_read,
        Scope.customers_write,
        Scope.orders_read,
        Scope.subscriptions_read,
        Scope.subscriptions_write,
    },
    allowed_subjects={User},
)
SearchRead = Annotated[AuthSubject[User], Depends(_SearchRead)]
