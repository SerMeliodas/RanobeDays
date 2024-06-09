from .models import Bookmark
from apps.novels.models import Novel
from apps.chapters.models import Chapter
from .types import BookmarkObject, BookmarkUpdateObject


def create_bookmark(data: BookmarkObject) -> Bookmark:
    novel = Novel.objects.get(pk=data.novel)
    chapter = Chapter.objects.get(pk=data.chapter)

    obj = Bookmark(user=data.user, novel=novel, chapter=chapter)

    obj.clean()
    obj.save()

    return obj


def update_bookmark(data: BookmarkUpdateObject):
    ...
