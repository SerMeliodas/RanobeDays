from django.urls import path, include

from apps.novels.apis.novel import (
    NovelListOrCreateAPI,
    NovelGetDeleteUpdateAPI
)


from apps.novels.apis.tag import (
    TagListOrCreateAPI,
    TagGetDeleteUpdateAPI
)


from apps.novels.apis.genre import (
    GenreListOrCreateAPI,
    GenreGetDeleteUpdateAPI
)


genre_patterns = [
    path('', GenreListOrCreateAPI.as_view(), name='list-or-create-genre'),
    path('<int:pk>/', GenreGetDeleteUpdateAPI.as_view(),
         name='get-delete-update-genre')
]


tag_patterns = [
    path('', TagListOrCreateAPI.as_view(), name='list-or-create-tag'),
    path('<int:pk>/', TagGetDeleteUpdateAPI.as_view(),
         name='get-delete-update-tag')
]


novel_patterns = [
    path('', NovelListOrCreateAPI.as_view(), name='list-or-create-novel'),
    path('<slug:slug>/', NovelGetDeleteUpdateAPI.as_view(),
         name='get-delete-update-novel')
]


urlpatterns = [
    path('novels/', include((novel_patterns, 'novels'))),
    path('tags/', include((tag_patterns, 'tags'))),
    path('genres/', include((genre_patterns, 'genres')))
]
