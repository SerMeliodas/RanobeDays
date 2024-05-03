from django.urls import path

from .apis import (
    LibraryAPI,
    LibraryDetailAPI
)


urlpatterns = [
    path('', LibraryAPI.as_view(), name='library'),
    path('<int:pk>/', LibraryDetailAPI.as_view(), name='library-detail')
]
