from django.urls import path, include

from .apis import (
    LibraryAPI,
    LibraryDetailAPI,
    LibraryItemAPI,
    LibraryItemDetailAPI
)


library_item_patterns = [
    path('', LibraryItemAPI.as_view(), name='library-item'),
    path('<int:pk>/', LibraryItemDetailAPI.as_view(),
         name='library-item-detail')
]


urlpatterns = [
    path('', LibraryAPI.as_view(), name='library'),
    path('<int:pk>/', LibraryDetailAPI.as_view(), name='library-detail'),
    path('library-items/', include(library_item_patterns), name='library-item')
]
