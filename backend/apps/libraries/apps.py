from django.apps import AppConfig


class LibrariesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.libraries'

    def ready(self):
        from . import signals
