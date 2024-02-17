from .models import Novel
from .dataclasses import NovelDTO


def create_novel(dto: NovelDTO) -> Novel:
    obj = Novel(title=dto.title)
    obj.isExist()
    obj.save()

    if dto.tags is not None:
        obj.tags.add(*[i['id'] for i in dto.tags])

    if dto.genres is not None:
        obj.genres.add(*[i['id'] for i in dto.genres])

    return obj
