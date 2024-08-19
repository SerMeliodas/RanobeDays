from apps.common.services import get_fields_to_update, model_update

from .types import BookmarkObject, BookmarkUpdateObject
from .models import Bookmark

import logging


logger = logging.getLogger(__name__)


def create_bookmark(data: BookmarkObject) -> Bookmark:
    obj = Bookmark(user=data.user, novel_id=data.novel,
                   chapter_id=data.chapter)

    obj.full_clean()
    obj.save()

    logger.info(f"Bookmark {obj.pk} was created")

    return obj


def update_bookmark(bookmark: Bookmark, data: BookmarkUpdateObject):
    fields = get_fields_to_update(data)

    bookmark, _ = model_update(instance=bookmark, fields=fields,
                               auto_updated_at=True, data=data.dict())

    logger.info(f"Bookmark {bookmark.pk} data: {data.dict()} was updated")

    return bookmark
