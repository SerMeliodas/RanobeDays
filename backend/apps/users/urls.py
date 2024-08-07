from django.urls import path, include

from .apis import (
    UserDetailAPI,
    UserPasswordDetailAPI
)

user_patterns = [
    path('', UserDetailAPI.as_view(), name='user-detail'),
    path('password/', UserPasswordDetailAPI.as_view(),
         name='user-password-detail'),
]

urlpatterns = [
    path('<str:username>/', include((user_patterns, 'user'))),
]
