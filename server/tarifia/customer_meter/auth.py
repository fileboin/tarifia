from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope
from tarifia.models.organization import Organization

_CustomerMeterRead = Authenticator(
    required_scopes={
        Scope.customer_meters_read,
    },
    allowed_subjects={User, Organization},
)
CustomerMeterRead = Annotated[
    AuthSubject[User | Organization], Depends(_CustomerMeterRead)
]
