from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="RanobeDays API",
        default_version="v1",
        description="The documentation for RanobeDays API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


docs_patterns = [
    path('',  schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
]


urlpatterns = [
    path('documentation/', include((docs_patterns, 'docs'), 'docs')),

    path('novels/', include(('apps.novels.urls', 'novels'), 'novels')),

    path('teams/', include(('apps.teams.urls', 'teams'), 'teams')),

    path('libraries/', include(('apps.libraries.urls', 'libraries'),
                               'libraries')),

    path('auth/', include(('apps.authentication.urls', 'auth'), 'auth')),

    path('auth/', include(('apps.oauth.urls', 'oauth'), 'oauth')),

    path('bookmarks/', include(('apps.bookmarks.urls',
         'bookmarks'), 'bookmarks')),

    path('metadata/', include(('apps.metadata.urls', 'metadata'), 'metadata')),

    path('users/', include(('apps.users.urls', 'users'), 'users')),

    path('notifications/', include(('apps.notifications.urls',
         'notifications'), 'notifications')),

    path('comments/', include(('apps.comments.urls', 'comments'), 'comments'))
]
