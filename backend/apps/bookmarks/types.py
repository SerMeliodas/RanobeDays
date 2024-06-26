from pydantic import BaseModel
from apps.users.models import User


class BookmarkObject(BaseModel):
    id: int | None = None
    user: User | None = None
    novel: int
    chapter: int

    class Config:
        arbitrary_types_allowed = True


class BookmarkUpdateObject(BaseModel):
    chapter: int | None = None
