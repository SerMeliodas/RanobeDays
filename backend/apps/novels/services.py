from .models import Novel, Tag, Genre
from .types import NovelDto, TagDto, GenreDto
from apps.common.services import model_update


def create_novel(dto: NovelDto) -> Novel:
    """Service for creating the novel instance"""
    obj = Novel(title=dto.title)
    obj.clean()
    obj.save()

    obj.genres.set(dto.genres)
    obj.tags.set(dto.tags)

    return obj


def update_novel(slug: str, dto: NovelDto) -> Novel:
    """Service for updating the novel instance"""
    novel = Novel.objects.get(slug=slug)
    fields = ['title', 'genres', 'tags']

    novel, _ = model_update(instance=novel, fields=fields,
                            data=dto.dict(),
                            auto_updated_at=True)

    return novel


def update_tag(pk: int, dto: TagDto) -> Tag:
    """Service for updating the tag instance"""
    tag = Tag.objects.get(pk=pk)

    fields = ['name']

    tag, _ = model_update(instance=tag, fields=fields,
                          data=dto.dict())

    return tag


def create_tag(dto: TagDto) -> Tag:
    obj = Tag(name=dto.name)
    obj.full_clean()
    obj.save()

    return obj


def create_genre(dto: GenreDto) -> Genre:
    obj = Genre(name=dto.name)
    obj.full_clean()
    obj.save()

    return obj


def update_genre(pk: int, dto: GenreDto) -> Genre:
    genre = Genre.objects.get(pk=pk)

    fields = ['name']

    genre, _ = model_update(instance=genre, fields=fields,
                            data=dto.dict())

    return genre
