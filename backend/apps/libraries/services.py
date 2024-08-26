from apps.common.services import model_update, get_fields_to_update

from .models import Library, LibraryItem
from .types import LibraryObject, LibraryItemObject

import logging


logger = logging.getLogger(__name__)


# service function thats create the new instance of Library model
def create_library(data: LibraryObject) -> Library:
    library = Library(name=data.name, user=data.user)
    library.save()

    logger.info(f"Library {data.name} was created")

    return library


# service function thats create the new instance of LibraryItem model
def create_library_item(data: LibraryItemObject) -> LibraryItem:
    item = LibraryItem(library_id=data.library, novel=data.novel)
    item.save()

    logger.info(f"Library item with Novel {
                data.novel} in Library({data.library})")

    return item


# service function thats update the instance of Library model
def update_library(library: Library, data: LibraryObject):
    library.name = data.name
    library.save()

    logger.info(f"Library {library.pk} data: {data.dict()} was updated")

    return library


# service function thats update the instance of LibraryItem model
def update_library_item(item: LibraryItem, data: LibraryItemObject):
    fields = get_fields_to_update(data)

    item, _ = model_update(instance=item, fields=fields,
                           data=data.dict(), auto_updated_at=True)

    logger.info(f"Library {item.pk} data: {data.dict()} was updated")

    return item
