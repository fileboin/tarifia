from typing import Annotated

from fastapi import Depends

from tarifia.auth.dependencies import Authenticator
from tarifia.auth.models import AuthSubject, User
from tarifia.auth.scope import Scope

_NotificationRecipientRead = Authenticator(
    required_scopes={
        Scope.notification_recipients_read,
        Scope.notification_recipients_write,
    },
    allowed_subjects={User},
)
NotificationRecipientRead = Annotated[
    AuthSubject[User], Depends(_NotificationRecipientRead)
]

_NotificationRecipientWrite = Authenticator(
    required_scopes={
        Scope.notification_recipients_write,
    },
    allowed_subjects={User},
)
NotificationRecipientWrite = Annotated[
    AuthSubject[User], Depends(_NotificationRecipientWrite)
]
