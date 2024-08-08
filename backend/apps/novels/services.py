from .models import Novel
from apps.metadata.models import Country, Language
from .types import NovelObject
from apps.common.services import model_update, get_fields_to_update
from django.db import transaction

import logging


logger = logging.getLogger(__name__)


@transaction.atomic
def create_novel(data: NovelObject) -> Novel:
    """Service for creating the novel instance"""
    novel = Novel(title=data.title, status=data.status,
                  country=Country.objects.get(pk=data.country),
                  language=Language.objects.get(pk=data.language))

    if data.original_title:
        novel.original_title = data.original_title

    if data.translate_language:
        novel.translate_language = Language.objects.get(
            pk=data.translate_language)

    if data.synopsys:
        novel.synopsys = data.synopsys

    novel.clean()
    novel.save()

    novel.genres.set(data.genres)
    novel.tags.set(data.tags)

    logger.info(f"Novel {novel.title} was created")

    return novel


def update_novel(novel: Novel, data: NovelObject) -> Novel:
    """Service for updating the novel instance"""
    fields = get_fields_to_update(data)

    novel, _ = model_update(instance=novel, fields=fields,
                            data=data.dict())

    logger.info(f"Novel {novel.title} data: {data.dict()} was updated")

    return novel
