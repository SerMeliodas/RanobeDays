from django.urls import path, include

from apps.novels.apis.novel import (
    NovelListApi,
    NovelGetApi,
    NovelCreatApi,
    NovelUpdateApi,
    NovelDeleteApi
)


from apps.novels.apis.tag import (
    TagListApi,
    TagGetApi,
    TagCreateApi,
    TagUpdateApi,
    TagDeleteApi
)


tag_patterns = [
    path('create/', TagCreateApi.as_view(), name='create new tag'),
    path('delete/<int:pk>/', TagDeleteApi.as_view(),
         name='delete tag instance'),
    path('update/<int:pk>/', TagUpdateApi.as_view(),
         name='update tag instance'),
    path('', TagListApi.as_view(), name='tag list'),
    path('<int:pk>/', TagGetApi.as_view(), name='get tag')
]


novel_patterns = [
    path('create/', NovelCreatApi.as_view(), name="create new novel"),
    path('delete/<int:pk>/', NovelDeleteApi.as_view(),
         name="delete novel instance"),
    path('update/<int:pk>/', NovelUpdateApi.as_view(),
         name="update novel instance"),
    path('', NovelListApi.as_view(), name="novels list"),
    path('<slug:slug>/', NovelGetApi.as_view(), name="get novel"),
]


urlpatterns = [
    path('novels/', include((novel_patterns, 'novels'))),
    path('tags/', include((tag_patterns, 'tags'))),
]
