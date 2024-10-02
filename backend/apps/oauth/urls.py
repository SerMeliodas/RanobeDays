from django.urls import path, include

from .apis import (
    GoogleLoginAPI,
    GoogleLoginRedirectAPI
)


google_urlpatterns = [
    path('login/', GoogleLoginRedirectAPI.as_view(), name='login'),
    path('login/callback', GoogleLoginAPI.as_view(), name='callback'),
]

urlpatterns = [
    path('google/', include((google_urlpatterns, 'google'), 'google')),
]
