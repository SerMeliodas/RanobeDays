from django.urls import path

from .apis import (
    CommentAPI,
    CommentDetailAPI
)


urlpatterns = [
    path('', CommentAPI.as_view(), name='comment'),
    path('<int:pk>/', CommentDetailAPI.as_view(), name='comment-detail')
]
