from django.contrib.auth import get_user_model

from apps.novels.models import Novel
from apps.common.services import model_update, get_fields_to_update

from .models import Library, LibraryItem
from .types import LibraryObject, LibraryItemObject


# service function thats create the new instance of Library model
def create_library(name: str, user: get_user_model()) -> Library:
    return Library(name=name, user=user).save()


# service function thats create the new instance of LibraryItem model
def create_library_item(library: Library, novel: Novel) -> LibraryItem:
    return LibraryItem(library=library, novel=novel).save()


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
                           data=data, auto_updated_at=True)

    return item
