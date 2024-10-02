from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .types import GoogleLoginCredentialsObject


def get_google_client_credentials() -> GoogleLoginCredentialsObject:
    client_id = settings.GOOGLE_CLIENT_ID
    project_id = settings.GOOGLE_CLIENT_PROJECT_ID
    secret = settings.GOOGLE_CLIENT_SECRET

    if not client_id:
        raise ImproperlyConfigured("GOOGLE_CLIENT_ID missing in env.")

    if not secret:
        raise ImproperlyConfigured("GOOGLE_CLIENT_SECRET missing in env.")

    if not project_id:
        raise ImproperlyConfigured("GOOGLE_PROJECT_ID missing in env.")

    return GoogleLoginCredentialsObject(
        client_id=client_id,
        project_id=project_id,
        secret=secret
    )
