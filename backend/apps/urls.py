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
    path('documentation/', include(docs_patterns)),

    # path('chapters/', include('apps.chapters.urls')),
    path('novels/', include('apps.novels.urls')),
    path('teams/', include('apps.teams.urls')),
    path('libraries/', include('apps.libraries.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('bookmarks/', include('apps.bookmarks.urls')),
    path('metadatas/', include('apps.metadata.urls')),
    path('users/', include(('apps.users.urls', 'users'), namespace='users'))
]
