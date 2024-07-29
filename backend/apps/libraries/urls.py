from django.urls import path, include

from .apis import (
    LibraryAPI,
    LibraryDetailAPI,
    LibraryItemAPI,
    LibraryItemDetailAPI
)


library_item_patterns = [
    path('', LibraryItemAPI.as_view(), name='library-item'),
    path('<int:library_item_id>/', LibraryItemDetailAPI.as_view(),
         name='library-item-detail')
]

library_detail_patterns = [
    path('', LibraryDetailAPI.as_view(), name='library-detail'),
    path('library-items/', include(library_item_patterns))
]


urlpatterns = [
    path('', LibraryAPI.as_view(), name='library'),
    path('<int:library_id>/', include(library_detail_patterns)),
]
