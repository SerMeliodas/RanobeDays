from django.urls import path, include
from .views import (
    NovelListApi,
    NovelGetApi,
    NovelCreatApi,
    NovelUpdateApi
)


novel_patterns = [
    path('create/', NovelCreatApi.as_view(), name="create new novel"),
    path('update/<int:pk>/', NovelUpdateApi.as_view(),
         name="update novel instance"),
    path('', NovelListApi.as_view(), name="novels list"),
    path('<slug:slug>/', NovelGetApi.as_view(), name="get novel"),
]


urlpatterns = [
    path('novels/', include((novel_patterns, 'novels'))),
]
