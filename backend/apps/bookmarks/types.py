from pydantic import BaseModel
from apps.users.models import User


class BookmarkObject(BaseModel):
    user: User
    chapter: int

    class Config:
        arbitrary_types_allowed = True
