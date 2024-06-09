from django.urls import path

from .apis import (
    BookmarkAPI
)

urlpatterns = [
    path('', BookmarkAPI.as_view(), name='bookmark')
]
