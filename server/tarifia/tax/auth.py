from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_TaxRead = Authenticator(
    required_scopes={Scope.transactions_read},
    allowed_subjects={User, Organization},
)
TaxRead = Annotated[AuthSubject[User | Organization], Depends(_TaxRead)]
