from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import (
    LoginView,
    LogoutView
)

register_patterns = [
    path('', RegisterView.as_view(), name='register'),
    # path('verify-email/'),
    # path('resend-email/')
]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', include((register_patterns, 'authentication')),
         name='register'),
    # TODO email confirmation endpoints
]
