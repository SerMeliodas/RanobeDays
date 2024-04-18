from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Library


DEFAULT_LIBRARY_NAMES = [
    'Читаю',
    'Буду читать',
    'Прочитано',
    'Любимые'
]


@receiver(post_save, sender=get_user_model())
def create_default_libraries(sender, ** kwargs):
    if kwargs['created']:
        for name in DEFAULT_LIBRARY_NAMES:
            Library(name=name, user=kwargs["instance"]).save()
