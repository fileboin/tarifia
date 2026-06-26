from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_PaymentRead = Authenticator(
    required_scopes={
        Scope.payments_read,
    },
    allowed_subjects={User, Organization},
)
PaymentRead = Annotated[AuthSubject[User | Organization], Depends(_PaymentRead)]
