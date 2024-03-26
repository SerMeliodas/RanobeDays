from django.urls import path

from .apis import (
    TranslatorTeamsListApi,
    TranslatorTeamsCreateApi,
)


urlpatterns = [
    path('', TranslatorTeamsListApi.as_view(), name="translator-teams-list"),
    path('create/', TranslatorTeamsCreateApi.as_view(),
         name="translator-teams-create"),
]
