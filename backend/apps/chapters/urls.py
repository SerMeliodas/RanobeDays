from django.urls import path


from .apis import (
    ChapterGetDeleteUpdateAPI,
    ChapterListOrCreateAPI
)


urlpatterns = [
    path('', ChapterListOrCreateAPI.as_view(), name='list-or-create-chapter'),
    path('<int:pk>', ChapterGetDeleteUpdateAPI.as_view(),
         name='get-delete-update-chpater')
]
