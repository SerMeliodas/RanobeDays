from .models import Novel, Tag


def tag_list() -> list[Tag]:
    return Tag.objects.all()


def get_tag(pk: int) -> Tag:
    return Tag.objects.get(pk=pk)


def novel_list() -> list[Novel]:
    return Novel.objects.all()


def get_novel(slug: str) -> Novel:
    return Novel.objects.get(slug=slug)
