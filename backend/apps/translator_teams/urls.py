from django.urls import path

from .apis import (
    TranslatorTeamsAPI,
    TranslatorTeamsDetailAPI
)


urlpatterns = [
    path('', TranslatorTeamsAPI.as_view(),
         name='list-or-create-translator-team'),
    path('<int:pk>', TranslatorTeamsDetailAPI.as_view(),
         name='get-delete-update-translator-team')
]
