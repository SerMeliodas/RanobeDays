from typing import TypedDict


class Genre(TypedDict):
    id: int


class Tag(TypedDict):
    id: int


class NovelDTO(TypedDict):
    title: str
    tags: list[Tag]
    genres: list[Genre]
