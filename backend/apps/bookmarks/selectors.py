from .models import Bookmark
from django.contrib.auth import get_user_model
from django.db.models import QuerySet


User = get_user_model()


def get_bookmark(pk: int) -> Bookmark:
    return Bookmark.objects.get(pk=pk)


def get_bookmarks(user: User) -> QuerySet[Bookmark]:
    return Bookmark.objects.filter(user=user)
