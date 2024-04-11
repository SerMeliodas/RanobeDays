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


urlpatterns = [
    path('', include('apps.novels.urls')),
    path('chapters/', include('apps.chapters.urls')),
    path('translator-teams/', include('apps.translator_teams.urls')),

    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0),
         name="schema-swagger-ui"),
    path('auth/', include('apps.authentication.urls')),
]
