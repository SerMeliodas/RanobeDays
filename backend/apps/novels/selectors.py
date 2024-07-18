from .models import Novel
import django_filters


class NovelFilter(django_filters.FilterSet):
    order_by = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('updated_at', 'updated'),
            ('created_at', 'added')
        )
    )

    tags = django_filters.NumberFilter(field_name='tags')
    genres = django_filters.NumberFilter(field_name='genres')

    class Meta:
        model = Novel
        fields = ['tags', 'genres']


def novel_list(*, filters=None):
    filters = filters or {}

    qs = Novel.objects.all()
    filter = NovelFilter(filters, qs)

    return filter.qs


def get_novel(slug: str) -> Novel:
    return Novel.objects.get(slug=slug)
