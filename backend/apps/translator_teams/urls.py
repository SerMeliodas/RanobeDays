from django.urls import path

from .apis import (
    TranslatorTeamsListOrCreateAPI,
    TranslatorTeamsGetDeleteUpdateAPI
)


urlpatterns = [
    path('', TranslatorTeamsListOrCreateAPI.as_view(),
         name='list-or-create-translator-team'),
    path('<int:pk>', TranslatorTeamsGetDeleteUpdateAPI.as_view(),
         name='get-delete-update-translator-team')
]
