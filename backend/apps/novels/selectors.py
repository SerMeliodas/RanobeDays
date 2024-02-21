from .models import Novel, Tag, Genre


def tag_list() -> list[Tag]:
    return Tag.objects.all()


def get_tag(pk: int) -> Tag:
    return Tag.objects.get(pk=pk)


def novel_list() -> list[Novel]:
    return Novel.objects.all()


def get_novel(slug: str) -> Novel:
    return Novel.objects.get(slug=slug)


def get_genre(pk: int) -> Genre:
    return Genre.objects.get(pk=pk)


def genre_list() -> list[Genre]:
    return Genre.objets.all()
