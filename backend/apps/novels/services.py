from .models import Novel, Tag, Genre
from .types import NovelObject, TagObject, GenreObject
from apps.common.services import model_update


def create_novel(data: NovelObject) -> Novel:
    """Service for creating the novel instance"""
    obj = Novel(title=data.title)
    obj.clean()
    obj.save()

    obj.genres.set(data.genres)
    obj.tags.set(data.tags)

    return obj


def update_novel(slug: str, data: NovelObject) -> Novel:
    """Service for updating the novel instance"""
    novel = Novel.objects.get(slug=slug)
    fields = ['title', 'genres', 'tags']

    novel, _ = model_update(instance=novel, fields=fields,
                            data=data.dict(),
                            auto_updated_at=True)

    return novel


def update_tag(pk: int, data: TagObject) -> Tag:
    """Service for updating the tag instance"""
    tag = Tag.objects.get(pk=pk)

    fields = ['name']

    tag, _ = model_update(instance=tag, fields=fields,
                          data=data.dict())

    return tag


def create_tag(data: TagObject) -> Tag:
    obj = Tag(name=data.name)
    obj.full_clean()
    obj.save()

    return obj


def create_genre(data: GenreObject) -> Genre:
    obj = Genre(name=data.name)
    obj.full_clean()
    obj.save()

    return obj


def update_genre(pk: int, data: GenreObject) -> Genre:
    genre = Genre.objects.get(pk=pk)

    fields = ['name']

    genre, _ = model_update(instance=genre, fields=fields,
                            data=data.dict())

    return genre
