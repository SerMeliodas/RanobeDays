from django.urls import path, include
from .views import (
    NovelListApi,
    NovelGetApi,
    NovelCreatApi
)


novel_patterns = [
    path('create/', NovelCreatApi.as_view(), name="create"),
    path('', NovelListApi.as_view(), name="list"),
    path('<slug:slug>/', NovelGetApi.as_view(), name="get"),
]


urlpatterns = [
    path('novels/', include((novel_patterns, 'novels'))),
]
