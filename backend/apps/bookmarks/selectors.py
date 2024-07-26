from .models import Bookmark
from apps.users.models import User


def get_bookmark(pk: int) -> Bookmark:
    return Bookmark.objects.get(pk=pk)


def get_bookmarks(user: User):
    return Bookmark.objects.filter(user=user)
