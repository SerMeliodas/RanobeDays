from pydantic import BaseModel


class TagDto(BaseModel):
    id: int | None = None
    name: str | None = None


class GenreDto(BaseModel):
    id: int | None = None
    name: str | None = None


class NovelDto(BaseModel):
    title: str
    tags: list[int]
    genres: list[int]
