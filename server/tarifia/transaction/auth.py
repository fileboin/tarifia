from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope

_TransactionsRead = Authenticator(
    required_scopes={
        Scope.transactions_read,
    },
    allowed_subjects={User},
)
TransactionsRead = Annotated[AuthSubject[User], Depends(_TransactionsRead)]

_TransactionsWrite = Authenticator(
    required_scopes={
        Scope.transactions_write,
    },
    allowed_subjects={User},
)
TransactionsWrite = Annotated[AuthSubject[User], Depends(_TransactionsWrite)]
