from pydantic import BaseModel


class LibraryObject(BaseModel):
    name: str | None = None
    user: int | None = None


class LibraryItemObject(BaseModel):
    library: int | None = None
    novel: int | None = None
