from .models import Chapter
from .types import ChapterObject

from apps.novels.models import Novel
from apps.teams.models import Team
from apps.common.services import model_update, get_fields_to_update

import logging


logger = logging.getLogger(__name__)


def create_chapter(data: ChapterObject) -> Chapter:
    novel = Novel.objects.get(slug=data.novel)
    team = Team.objects.get(pk=data.team)

    chapter = Chapter(title=data.title, novel=novel, text=data.text,
                      team=team, number=data.number, volume=data.volume)
    chapter.full_clean()
    chapter.save()

    logger.info(f"Chapter {chapter.pk} for novel {novel.pk} was created")

    return chapter


def update_chapter(data: ChapterObject, pk: int) -> Chapter:
    chapter = Chapter.objects.get(pk=pk)

    fields = get_fields_to_update(data)

    chapter, _ = model_update(instance=chapter, fields=fields,
                              data=data.dict(), auto_updated_at=True)

    logger.info(f"Chapter {chapter.pk} data: {data.dict()} was updated")

    return chapter
