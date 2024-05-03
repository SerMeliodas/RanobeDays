from .models import Library, LibraryItem
from django.db.models import QuerySet


def get_library(pk: int) -> Library:
    return Library.objects.get(pk=pk)


def get_libraries() -> QuerySet:
    return Library.objects.all()


def get_library_item(pk: int) -> LibraryItem:
    return LibraryItem.objects.get(pk=pk)
