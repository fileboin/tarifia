from pydantic import UUID4

from tarifia.kit.schemas import Schema
from tarifia.notifications.notification import Notification


class NotificationsList(Schema):
    notifications: list[Notification]
    last_read_notification_id: UUID4 | None


class NotificationsMarkRead(Schema):
    notification_id: UUID4
