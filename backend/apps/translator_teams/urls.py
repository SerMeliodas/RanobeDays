from django.urls import path

from .apis import (
    TranslatorTeamsListApi,
    TranslatorTeamsCreateApi,
    TranslatorTeamsDeleteApi,
    TranslatorTeamsUpdateApi,
)


urlpatterns = [
    path('', TranslatorTeamsListApi.as_view(),
         name='translator-teams-list'),
    path('create/', TranslatorTeamsCreateApi.as_view(),
         name='translator-teams-create'),
    path('delete/<int:pk>/', TranslatorTeamsDeleteApi.as_view(),
         name='translator-teams-delete'),
    path('update/<int:pk>/', TranslatorTeamsUpdateApi.as_view(),
         name='translator-teams-update'),
]
