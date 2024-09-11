from django.urls import path, include

from .apis import (
    UserDetailAPI,
    UserPasswordDetailAPI,
    RequestPasswordResetAPI,
    ResetPasswordAPI
)

password_patterns = [
    path('request/',  RequestPasswordResetAPI.as_view(),
         name='request-password-reset'),
    path('reset/<str:uid>/<str:token>/', ResetPasswordAPI.as_view(),
         name='reset-password'),
]

user_patterns = [
    path('', UserDetailAPI.as_view(), name='user-detail'),
    path('password/', UserPasswordDetailAPI.as_view(),
         name='user-password-detail'),
]

urlpatterns = [
    path('password/', include((password_patterns, 'password'), 'password')),
    path('<str:username>/', include((user_patterns, 'user'))),
]
