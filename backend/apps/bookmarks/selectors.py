from .models import Bookmark
from apps.users.models import User
from django.db.models import QuerySet


def get_bookmark(pk: int) -> Bookmark:
    return Bookmark.objects.get(pk=pk)


def get_bookmarks(user: User) -> QuerySet[Bookmark]:
    return Bookmark.objects.filter(user=user)
