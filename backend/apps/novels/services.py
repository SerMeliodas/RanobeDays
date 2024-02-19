from .models import Novel
from .types import NovelDTO


def create_novel(dto: NovelDTO) -> Novel:
    obj = Novel(title=dto.title)
    obj.isExist()
    obj.save()

    if dto.tags is not None:
        obj.tags.add(*[i.id for i in dto.tags])

    if dto.genres is not None:
        obj.genres.add(*[i.id for i in dto.genres])

    return obj


def update_novel(pk: int, dto: NovelDTO) -> Novel:
    novel = Novel.objects.get(pk=pk)
    fields = ['title', 'genres', 'tags']

    novel, updated = model_update(instance=novel, fields=fields,
                                  data=dto.dict(),
                                  auto_updated_at=True)

    return novel
