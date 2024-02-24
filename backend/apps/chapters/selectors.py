from .models import Chapter
from apps.novels.models import Novel


def get_chapters_list_by_novel(novel: Novel) -> Chapter:
    return Chapter.objects.all().filter(novel=novel)


def get_chapters_list() -> Chapter:
    return Chapter.objects.all()


def get_chapter_by_id(pk: int) -> Chapter:
    return Chapter.objects.get(pk=pk)
