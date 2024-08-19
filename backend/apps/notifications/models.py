from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


from apps.common.models import BaseModel


class Notification(BaseModel):
    TYPES = (
        ('updates', _('Updates')),
        ('important', _('Important'))
    )

    notification_type = models.CharField(max_length=20, choices=TYPES)
    novel = models.ForeignKey(
        'novels.Novel', on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(
        get_user_model(), related_name='notifications',
        on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        db_table = 'notifications'
        ordering = ['-created_at']
