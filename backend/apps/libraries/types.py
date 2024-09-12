from pydantic import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class LibraryObject(BaseModel):
    name: str | None = None
    user: User | None = None

    class Config:
        arbitrary_types_allowed = True


class LibraryItemObject(BaseModel):
    library: int | None = None
    novel: int | None = None
