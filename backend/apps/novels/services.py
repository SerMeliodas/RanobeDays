from .models import Novel
from .types import NovelObject

from apps.common.services import model_update, get_fields_to_update

from apps.metadata.models import Language
from django.db import transaction

import logging


logger = logging.getLogger(__name__)


@transaction.atomic
def create_novel(data: NovelObject) -> Novel:
    """Service for creating the novel instance"""
    novel = Novel(title=data.title, status=data.status,
                  country_id=data.country,
                  language_id=data.language,
                  creator_id=data.creator)

    if data.original_title:
        novel.original_title = data.original_title

    if data.translated_language:
        novel.translated_language = Language.objects.get(
            pk=data.translated_language)

    if data.synopsys:
        novel.synopsys = data.synopsys

    novel.clean()
    novel.save()

    novel.genres.set(data.genres)
    novel.tags.set(data.tags)

    novel.teams.set([data.creator])

    logger.info(f"Novel {novel.title} was created")

    return novel


def update_novel(novel: Novel, data: NovelObject) -> Novel:
    """Service for updating the novel instance"""
    fields = get_fields_to_update(data)

    novel, _ = model_update(instance=novel, fields=fields,
                            data=data.dict())

    logger.info(f"Novel {novel.title} data: {data.dict()} was updated")

    return novel
