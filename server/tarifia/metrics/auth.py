from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

_MetricsRead = Authenticator(
    required_scopes={Scope.metrics_read},
    allowed_subjects={User, Organization},
)
MetricsRead = Annotated[AuthSubject[User | Organization], Depends(_MetricsRead)]

_MetricsWrite = Authenticator(
    required_scopes={Scope.metrics_write},
    allowed_subjects={User, Organization},
)
MetricsWrite = Annotated[AuthSubject[User | Organization], Depends(_MetricsWrite)]
