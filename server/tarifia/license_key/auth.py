from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, Organization, User
from tarifia.auth.scope import Scope

LicenseKeysRead = Annotated[
    AuthSubject[User | Organization],
    Depends(
        Authenticator(
            required_scopes={
                Scope.license_keys_read,
                Scope.license_keys_write,
            },
            allowed_subjects={User, Organization},
        )
    ),
]

LicenseKeysWrite = Annotated[
    AuthSubject[User | Organization],
    Depends(
        Authenticator(
            required_scopes={
                Scope.license_keys_write,
            },
            allowed_subjects={User, Organization},
        )
    ),
]
