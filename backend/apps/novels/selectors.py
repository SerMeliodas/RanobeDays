from .models import Novel
from typing import Iterable


def novel_list() -> Iterable[Novel]:
    return Novel.objects.all()


def get_novel(slug: str) -> Novel:
    return Novel.objects.get(slug=slug)
