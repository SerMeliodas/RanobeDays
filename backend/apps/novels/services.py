from .models import Novel
from .types import NovelDTO
from apps.common.services import model_update


def create_novel(dto: NovelDTO) -> Novel:
    obj = Novel(title=dto.title)
    obj.isExist()
    obj.save()

    obj.genres.set(dto.genres)
    obj.tags.set(dto.tags)

    return obj


def update_novel(pk: int, dto: NovelDTO) -> Novel:
    novel = Novel.objects.get(pk=pk)
    fields = ['title', 'genres', 'tags']

    novel, updated = model_update(instance=novel, fields=fields,
                                  data=dto.dict(),
                                  auto_updated_at=True)

    return novel
