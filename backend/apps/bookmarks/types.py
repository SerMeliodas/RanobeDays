from pydantic import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class BookmarkObject(BaseModel):
    user: User
    chapter: int

    class Config:
        arbitrary_types_allowed = True
