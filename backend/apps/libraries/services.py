from apps.common.services import model_update, get_fields_to_update

from apps.novels.models import Novel
from .models import Library, LibraryItem
from .types import LibraryObject, LibraryItemObject


# service function thats create the new instance of Library model
def create_library(data: LibraryObject) -> Library:
    library = Library(name=data.name, user=data.user)
    library.save()
    return library


# service function thats create the new instance of LibraryItem model
def create_library_item(data: LibraryItemObject) -> LibraryItem:
    library = Library(pk=data.library)
    novel = Novel(pk=data.novel)
    item = LibraryItem(library=library, novel=novel)
    item.save()
    return item


# service function thats update the instance of Library model
def update_library(pk: int, data: LibraryObject):
    library = Library.objects.get(pk=pk)

    fields = get_fields_to_update(data)

    library, _ = model_update(instance=library, fields=fields,
                              data=data.dict())

    return library


# service function thats update the instance of LibraryItem model
def update_library_item(pk: int, data: LibraryItemObject):
    item = LibraryItem.objects.get(pk=pk)

    fields = get_fields_to_update(data)

    item, _ = model_update(instance=item, fields=fields,
                           data=data.dict(), auto_updated_at=True)

    return item
