from django.urls import path, include

from .apis import (
    NovelAPI,
    NovelDetailAPI
)


novel_patterns = [
    path('', NovelAPI.as_view(), name='list-or-create-novel'),
    path('<slug:slug>/', NovelDetailAPI.as_view(),
         name='get-delete-update-novel')
]


urlpatterns = [
    path('novels/', include((novel_patterns, 'novels'))),
]
