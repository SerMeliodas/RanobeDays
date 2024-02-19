from pydantic import BaseModel


class TagDTO(BaseModel):
    id: int | None = None
    name: str | None = None


class GenreDTO(BaseModel):
    id: int | None = None
    name: str | None = None


class NovelDTO(BaseModel):
    title: str
    tags: list[int]
    genres: list[int]
