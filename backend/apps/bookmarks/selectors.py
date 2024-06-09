from .models import Bookmark


def get_bookmark(pk: int) -> Bookmark:
    return Bookmark.objects.get(pk=pk)


def get_bookmarks():
    return Bookmark.objects.all()
