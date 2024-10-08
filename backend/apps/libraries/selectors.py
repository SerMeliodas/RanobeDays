from .models import Library, LibraryItem
from django.db.models import QuerySet
import django_filters


class LibraryFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(
        field_name="user__username", lookup_expr="exact")

    class Meta:
        model = Library
        fields = ['user']


def get_library(pk: int) -> Library:
    return Library.objects.get(pk=pk)


def get_libraries(*, filters) -> QuerySet:
    filters = filters or {}

    filter = LibraryFilter(filters, queryset=Library.objects.all())

    return filter.qs


def get_library_item(pk: int) -> LibraryItem:
    return LibraryItem.objects.get(pk=pk)


def get_library_items(library_id: int) -> QuerySet:
    return LibraryItem.objects.filter(library__pk=library_id)
