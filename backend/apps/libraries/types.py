from pydantic import BaseModel
from apps.users.models import User


class LibraryObject(BaseModel):
    name: str | None = None
    user: User | None = None

    class Config:
        arbitrary_types_allowed = True


class LibraryItemObject(BaseModel):
    library: int | None = None
    novel: int | None = None
