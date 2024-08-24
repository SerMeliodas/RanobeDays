from .models import Chapter
from .types import ChapterObject

from apps.common.services import model_update, get_fields_to_update

import logging


logger = logging.getLogger(__name__)


def create_chapter(data: ChapterObject) -> Chapter:
    chapter = Chapter(title=data.title, novel_id=data.novel, text=data.text,
                      team_id=data.team, number=data.number,
                      volume=data.volume)
    chapter.full_clean()
    chapter.save()

    logger.info(f"Chapter {chapter.pk} for novel {data.novel} was created")

    return chapter


def update_chapter(chapter: Chapter, data: ChapterObject) -> Chapter:
    fields = get_fields_to_update(data)

    chapter, _ = model_update(instance=chapter, fields=fields,
                              data=data.dict(), auto_updated_at=True)

    logger.info(f"Chapter {chapter.pk} data: {data.dict()} was updated")

    return chapter
