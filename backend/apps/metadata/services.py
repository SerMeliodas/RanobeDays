import logging

from .models import Tag, Genre, Language, Country
from .types import TagObject, GenreObject, LanguageObject, CountryObject

from apps.common.services import model_update, get_fields_to_update

logger = logging.getLogger(__name__)


def update_tag(pk: int, data: TagObject) -> Tag:
    """Service for updating the tag instance"""
    tag = Tag.objects.get(pk=pk)

    fields = ['name']

    tag, _ = model_update(instance=tag, fields=fields,
                          data=data.dict())

    logger.info(f"Tag {tag.pk}  data: {data.name} was updated")

    return tag


def create_tag(data: TagObject) -> Tag:
    obj = Tag(name=data.name)
    obj.full_clean()
    obj.save()

    logger.info(f"Tag {data.name} was created")

    return obj


def create_genre(data: GenreObject) -> Genre:
    obj = Genre(name=data.name)
    obj.full_clean()
    obj.save()

    logger.info(f"Genre {data.name} was created")

    return obj


def update_genre(pk: int, data: GenreObject) -> Genre:
    genre = Genre.objects.get(pk=pk)

    fields = ['name']

    genre, _ = model_update(instance=genre, fields=fields,
                            data=data.dict())

    logger.info(f"Genre {genre.pk}  data: {data.name} was updated")

    return genre


def create_language(data: LanguageObject) -> Language:
    obj = Language(name=data.name, abbreviation=data.abbreviation)
    obj.clean()
    obj.save()

    logger.info(f"Language {data.name} was created")

    return obj


def update_language(pk: int, data: LanguageObject) -> Language:
    obj = Language.objects.get(pk=pk)

    fields = get_fields_to_update(data)

    obj, _ = model_update(instance=obj, fields=fields,
                          data=data.dict())

    logger.info(f"Language {obj.pk}  data: {data.name} was updated")

    return obj


def create_country(data: CountryObject) -> Country:
    obj = Country(name=data.name)
    obj.clean()
    obj.save()

    logger.info(f"Country {data.name} was created")

    return obj


def update_country(pk: int, data: CountryObject) -> Country:
    obj = Country.objects.get(pk=pk)

    fields = ['name']

    obj, _ = model_update(instance=obj, fields=fields,
                          data=data.dict())

    logger.info(f"Counrtry {obj.pk}  data: {data.name} was updated")

    return obj
