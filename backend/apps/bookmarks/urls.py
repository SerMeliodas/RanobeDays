from django.urls import path

from .apis import (
    BookmarkAPI,
    BookmarkDetailAPI
)

urlpatterns = [
    path('', BookmarkAPI.as_view(), name='bookmark'),
    path('<int:pk>/', BookmarkDetailAPI.as_view(), name='bookmark-detail')
]
