from .models import Chapter
from django.db.models import QuerySet
import django_filters


class ChapterFilter(django_filters.FilterSet):
    novel = django_filters.NumberFilter(field_name='novel')
    order_by = django_filters.OrderingFilter(
        fields=(
            ('updated_at', 'updated'),
            ('created_at', 'added')
        )
    )

    class Meta:
        model = Chapter
        fields = ('novel', )


def get_chapters_list(*, filters=None) -> QuerySet:
    filters = filters or {}

    qs = Chapter.objects.all()
    filter = ChapterFilter(filters, qs)

    return filter.qs


def get_chapter_by_id(pk: int) -> Chapter:
    return Chapter.objects.get(pk=pk)
