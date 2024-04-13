from pydantic import BaseModel


class TagObject(BaseModel):
    id: int | None = None
    name: str | None = None


class GenreObject(BaseModel):
    id: int | None = None
    name: str | None = None


class NovelObject(BaseModel):
    title: str | None = None
    tags: list[int] | None = None
    genres: list[int] | None = None
