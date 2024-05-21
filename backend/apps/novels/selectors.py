from .models import Novel, Tag, Genre
import django_filters


class NovelFilter(django_filters.FilterSet):
    tags = django_filters.NumberFilter(field_name='tags')
    genres = django_filters.NumberFilter(field_name='genres')

    class Meta:
        model = Novel
        fields = ['tags', 'genres']


def tag_list() -> list[Tag]:
    return Tag.objects.all()


def get_tag(pk: int) -> Tag:
    return Tag.objects.get(pk=pk)


def novel_list(*, filters=None):
    filters = filters or {}

    qs = Novel.objects.all()
    filter = NovelFilter(filters, qs)

    return filter.qs


def get_novel(slug: str) -> Novel:
    return Novel.objects.get(slug=slug)


def get_genre(pk: int) -> Genre:
    return Genre.objects.get(pk=pk)


def genre_list() -> list[Genre]:
    return Genre.objects.all()
