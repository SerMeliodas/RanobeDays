from .types import BookmarkObject
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
