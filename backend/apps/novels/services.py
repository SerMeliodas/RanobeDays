from .models import Novel, Tag, Genre
from .types import NovelDTO, TagDTO, GenreDTO
from apps.common.services import model_update


def create_novel(dto: NovelDTO) -> Novel:
    """Service for creating the novel instance"""
    obj = Novel(title=dto.title)
    obj.clean()
    obj.save()

    obj.genres.set(dto.genres)
    obj.tags.set(dto.tags)

    return obj


def update_novel(pk: int, dto: NovelDTO) -> Novel:
    """Service for updating the novel instance"""
    novel = Novel.objects.get(pk=pk)
    fields = ['title', 'genres', 'tags']

    novel, _ = model_update(instance=novel, fields=fields,
                            data=dto.dict(),
                            auto_updated_at=True)

    return novel


def update_tag(pk: int, dto: TagDTO) -> Tag:
    """Service for updating the tag instance"""
    tag = Tag.objects.get(pk=pk)

    fields = ['name']

    tag, _ = model_update(instance=tag, fields=fields,
                          data=dto.dict())

    return tag


def create_tag(dto: TagDTO) -> Tag:
    obj = Tag(name=dto.name)
    obj.full_clean()
    obj.save()

    return obj


def create_genre(dto: GenreDTO) -> Genre:
    obj = Genre(name=dto.name)
    obj.full_clean()
    obj.save()

    return obj


def update_genre(pk: int, dto: GenreDTO) -> Genre:
    genre = Genre.objects.get(pk=pk)

    fields = ['name']

    genre, _ = model_update(instance=genre, fields=fields,
                            data=dto.dict())

    return genre
