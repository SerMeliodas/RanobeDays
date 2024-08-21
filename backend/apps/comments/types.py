from pydantic import BaseModel
from apps.users.models import User


class CommentObject(BaseModel):
    comment_type: str
    message: str

    user: User

    novel: str | None = None
    chapter: int | None = None

    parent: int | None = None

    class Config:
        arbitrary_types_allowed = True
