from django.urls import path, include

from .apis import (
    NovelAPI,
    NovelDetailAPI
)
from apps.chapters.apis import (
    ChapterAPI,
    ChapterDetailAPI
)

chapter_patterns = [
    path('', ChapterAPI.as_view(), name='list-create-chapter'),
    path('<int:pk>/', ChapterDetailAPI.as_view(),
         name='get-delete-update-chapter')
]

novel_detail_patterns = [
    path('', NovelDetailAPI.as_view(), name='get-delete-update-novel'),
    path('chapters/', include((chapter_patterns, 'chapters')))
]


novel_patterns = [
    path('', NovelAPI.as_view(), name='list-or-create-novel'),
    path('<slug:slug>/', include((novel_detail_patterns, 'novel-detail')))
]


urlpatterns = [
    path('novels/', include((novel_patterns, 'novels'))),
]
