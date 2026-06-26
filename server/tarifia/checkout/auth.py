from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import Anonymous, AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_CheckoutRead = Authenticator(
    required_scopes={
        Scope.checkouts_read,
        Scope.checkouts_write,
    },
    allowed_subjects={User, Organization},
)
CheckoutRead = Annotated[AuthSubject[User | Organization], Depends(_CheckoutRead)]

_CheckoutWrite = Authenticator(
    required_scopes={Scope.checkouts_write},
    allowed_subjects={User, Organization},
)
CheckoutWrite = Annotated[AuthSubject[User | Organization], Depends(_CheckoutWrite)]

_CheckoutWeb = Authenticator(
    required_scopes=set(),
    allowed_subjects={User, Anonymous},
)
CheckoutWeb = Annotated[AuthSubject[User | Anonymous], Depends(_CheckoutWeb)]
