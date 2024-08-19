from .models import Notification


def get_notifications(user):
    return Notification.objects.filter(user=user)


def get_notification(pk: int):
    return Notification.objects.get(pk=pk)
