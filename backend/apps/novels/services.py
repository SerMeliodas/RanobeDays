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
    obj = Novel(title=data.title, status=data.status,
                country=Country.objects.get(pk=data.country),
                language=Language.objects.get(pk=data.language))

    if data.original_title:
        obj.original_title = data.original_title

    if data.translate_language:
        obj.translate_language = Language.objects.get(
            pk=data.translate_language)

    if data.synopsys:
        obj.synopsys = data.synopsys

    obj.clean()
    obj.save()

    obj.genres.set(data.genres)
    obj.tags.set(data.tags)

    logger.info(f"Novel {obj.title} was created")

    return obj


def update_novel(slug: str, data: NovelObject) -> Novel:
    """Service for updating the novel instance"""
    novel = Novel.objects.get(slug=slug)

    fields = get_fields_to_update(data)

    novel, _ = model_update(instance=novel, fields=fields,
                            data=data.dict())

    logger.info(f"Novel {novel.title} data: {data.dict()} was updated")

    return novel
