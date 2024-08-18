from django.urls import path, include

from .apis import (
    NovelAPI,
    NovelDetailAPI
)

from apps.chapters.apis import (
    ChapterAPI,
    ChapterDetailAPI
)

from apps.teams.apis import (
    TeamsNovelAPI,
    TeamsNovelDetailAPI
)

teams_patterns = [
    path('', TeamsNovelAPI.as_view(), name='teams'),
    path('<int:pk>/', TeamsNovelDetailAPI.as_view(), name='teams-detail')
]

chapter_patterns = [
    path('', ChapterAPI.as_view(), name='chapter'),
    path('<int:pk>/', ChapterDetailAPI.as_view(),
         name='detail-chapter'),
]

novel_detail_patterns = [
    path('', NovelDetailAPI.as_view(), name='detail'),
    path('chapters/', include((chapter_patterns, 'chapters'))),
    path('teams/', include((teams_patterns, 'teams')))
]


novel_patterns = [
    path('', NovelAPI.as_view(), name='list-or-create-novel'),
    path('<slug:slug>/', include((novel_detail_patterns, 'novel-detail')))
]


urlpatterns = [
    path('', include((novel_patterns, 'novels'))),
]
