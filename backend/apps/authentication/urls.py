from django.urls import path

from .apis import (
    AuthRegisterAPI,
    AuthLoginAPI,
    AuthLogoutAPI,

    SendEmailVerificationAPI,
    VerifyEmailAPI
)

urlpatterns = [
    path('login/', AuthLoginAPI.as_view(), name='login'),
    path('register/', AuthRegisterAPI.as_view(), name='register'),
    path('logout/', AuthLogoutAPI.as_view(), name='logout'),

    path('send-email/', SendEmailVerificationAPI.as_view(),
         name='send-verification-email'),
    path('verify-email/', VerifyEmailAPI.as_view(), name='verify-email')
]
