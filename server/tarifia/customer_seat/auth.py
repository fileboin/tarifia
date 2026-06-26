from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_SeatRead = Authenticator(
    required_scopes={
        Scope.customer_seats_read,
    },
    allowed_subjects={User, Organization},
)
SeatRead = Annotated[AuthSubject[User | Organization], Depends(_SeatRead)]

_SeatWrite = Authenticator(
    required_scopes={
        Scope.customer_seats_write,
    },
    allowed_subjects={User, Organization},
)
SeatWrite = Annotated[AuthSubject[User | Organization], Depends(_SeatWrite)]
