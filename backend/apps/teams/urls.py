from django.urls import path

from .apis import (
    TeamsAPI,
    TeamsDetailAPI,
)


urlpatterns = [
    path('', TeamsAPI.as_view(),
         name='team'),
    path('<int:pk>/', TeamsDetailAPI.as_view(),
         name='team-detail')
]
