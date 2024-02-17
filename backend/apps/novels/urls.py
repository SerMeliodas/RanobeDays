from django.urls import path, include
from .views import (
    NovelListApi,
    NovelGetApi,
    NovelCreatApi
)


novel_patterns = [
    path('create/', NovelCreatApi.as_view(), name="create new novel"),
    path('', NovelListApi.as_view(), name="novels list"),
    path('<slug:slug>/', NovelGetApi.as_view(), name="get novel"),
]


urlpatterns = [
    path('novels/', include((novel_patterns, 'novels'))),
]
