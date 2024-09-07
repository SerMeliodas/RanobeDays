from django.urls import path, include

from .apis import email_confirm_redirect

from dj_rest_auth.registration.views import (
    RegisterView,
    VerifyEmailView,
    ResendEmailVerificationView
)
from dj_rest_auth.views import (
    LoginView,
    LogoutView
)

register_patterns = [
    path('', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(),
         name='resend_email'),
]

urlpatterns = [
    path('confirm-email/<str:key>/', email_confirm_redirect,
         name='account_confirm_email'),
    path('confirm-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', include((register_patterns, 'register')),
         name='register'),
]
