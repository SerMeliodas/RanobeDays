from .models import Chapter
from apps.novels.models import Novel


def get_chapters_list_by_novel(novel_id: int) -> Chapter:
    novel = Novel.objects.get(pk=novel_id)
    return Chapter.objects.all().filter(novel=novel)


def get_chapter_by_id(pk: int) -> Chapter:
    return Chapter.objects.get(pk=pk)
