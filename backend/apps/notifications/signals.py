from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.chapters.models import Chapter
from apps.libraries.models import Library, LibraryItem
from .models import Notification


@receiver(post_save, sender=Chapter)
def notification_send(sender, **kwargs):
    if kwargs['created']:
        users = Library.objects.filter(items__in=LibraryItem.objects.filter(
            novel=kwargs['instance'].novel)).values_list('user', flat=True)

        for user in users:
            Notification.objects.create(
                notification_type='update',
                novel=kwargs['instance'].novel,
                message=f'{kwargs['instance'].novel} was updated: chapter {
                    kwargs['instance'].volume}:{kwargs['instance'].number} was added',
                user_id=user
            )
