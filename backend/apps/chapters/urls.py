from django.urls import path

from .apis import (
    ChapterCreateApi,
    ChapterGetApi,
    ChapterDeleteApi,
    ChapterGetListByNovelApi,
    ChapterUpdateApi
)


urlpatterns = [
    path('<int:pk>/', ChapterGetApi.as_view(),
         name='get chapter instance by id'),
    path('novel/<int:novel_id>/', ChapterGetListByNovelApi.as_view(),
         name='get novel chapters'),
    path('create/', ChapterCreateApi.as_view(),
         name='create chapter instance'),
    path('delete/<int:pk>/', ChapterDeleteApi.as_view(),
         name='delete chapter instance'),
    path('update/<int:pk>/', ChapterUpdateApi.as_view(),
         name='update chapter instance'),
]
