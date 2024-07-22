from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.conf import settings


from .types import LibraryObject

from .services import (
    create_library
)


@receiver(post_save, sender=get_user_model())
def create_default_libraries(sender, ** kwargs):
    if kwargs['created']:
        for name in settings.DEFAULT_LIBRARY_NAMES:
            library = LibraryObject(name=name, user=kwargs['instance'])
            create_library(library)
