from .models import Novel
from .types import NovelDTO


def create_novel(dto: NovelDTO) -> Novel:
    obj = Novel(title=dto['title'])
    obj.isExist()
    obj.save()

    if dto['tags'] is not None:
        obj.tags.set([i['id'] for i in dto['tags']])

    if dto['genres'] is not None:
        obj.genres.set([i['id'] for i in dto['genres']])

    return obj


# TODO: implement update_novel function
def update_novel(pk: int, dto: NovelDTO) -> Novel:
    return Novel()
