from .models import Chapter
from django.db.models import QuerySet


def get_chapters_list() -> QuerySet:
    return Chapter.objects.all()


def get_chapter_by_id(pk: int) -> Chapter:
    return Chapter.objects.get(pk=pk)
