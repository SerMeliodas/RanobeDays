from django.urls import path

from .apis import (
    ChapterCreateAPI,
    ChapterGetAPI,
    ChapterDeleteAPI,
    ChapterGetListByNovelAPI,
    ChapterUpdateAPI
)


urlpatterns = [
    path('<int:pk>/', ChapterGetAPI.as_view(),
         name='get chapter instance by id'),
    path('novel/<int:novel_id>/', ChapterGetListByNovelAPI.as_view(),
         name='get novel chapters'),
    path('create/', ChapterCreateAPI.as_view(),
         name='create chapter instance'),
    path('delete/<int:pk>/', ChapterDeleteAPI.as_view(),
         name='delete chapter instance'),
    path('update/<int:pk>/', ChapterUpdateAPI.as_view(),
         name='update chapter instance'),
]
