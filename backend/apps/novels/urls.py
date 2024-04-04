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
    GenreGetAPI,
    GenreListAPI,
    GenreUpdateAPI,
    GenreDeleteAPI,
    GenreCreateAPI
)


genre_patterns = [
    path('create/', GenreCreateAPI.as_view(), name='create new genre'),
    path('delete/<int:pk>/', GenreDeleteAPI.as_view(),
         name='delete genre instance'),
    path('update/<int:pk>/', GenreUpdateAPI.as_view(),
         name='update genre instance'),
    path('', GenreListAPI.as_view(), name='genre list'),
    path('<int:pk>/', GenreGetAPI.as_view(), name='get genre')
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
