from .models import Notification
from .types import NotificationObject
from apps.common.services import get_fields_to_update, model_update


def create_notification(data: NotificationObject):
    notification = Notification(notification_type=data.notification_type,
                                user=data.user)

    if data.novel:
        notification.novel = data.novel

    if data.message:
        notification.message = data.message

    notification.save()

    return notification


def update_notification(notification, data: NotificationObject):
    fields = get_fields_to_update(data)

    notification, _ = model_update(instance=notification, fields=fields,
                                   auto_updated_at=True)

    return notification
