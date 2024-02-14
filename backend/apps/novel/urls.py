from django.urls import path, include


urlpatterns = [
    path('novel/', include('apps.novel.urls'))
]
