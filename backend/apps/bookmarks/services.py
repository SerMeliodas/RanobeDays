from apps.novels.models import Novel
from apps.chapters.models import Chapter
from apps.common.services import get_fields_to_update, model_update

from .types import BookmarkObject, BookmarkUpdateObject
from .models import Bookmark


def create_bookmark(data: BookmarkObject) -> Bookmark:
    novel = Novel.objects.get(pk=data.novel)
    chapter = Chapter.objects.get(pk=data.chapter)

    obj = Bookmark(user=data.user, novel=novel, chapter=chapter)

    obj.clean()
    obj.save()

    return obj


def update_bookmark(pk: int, data: BookmarkUpdateObject):
    bookmark = Bookmark.objects.get(pk=pk)

    fields = get_fields_to_update(data)

    bookmark, _ = model_update(instance=bookmark, fields=fields,
                               auto_updated_at=True, data=data.dict())

    return bookmark
