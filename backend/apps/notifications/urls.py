from django.urls import path

from .apis import (
    NotificationAPI,
    NotificationDetailAPI
)


urlpatterns = [
    path('', NotificationAPI.as_view(), name='notification'),
    path('<int:pk>/', NotificationDetailAPI.as_view(), name='notification-detail'),
]
