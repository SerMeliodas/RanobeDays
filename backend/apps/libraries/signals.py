from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from .types import LibraryObject

from .services import (
    create_library
)

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
            library = LibraryObject(name=name, user=kwargs['instance'])
            create_library(library)
