from pydantic import BaseModel


class Tag(BaseModel):
    id: int
    name: str | None = None


class Genre(BaseModel):
    id: int
    name: str | None = None


class NovelDTO(BaseModel):
    title: str
    tags: list[int]
    genres: list[int]
