from dataclasses import dataclass
from typing import TypedDict


class Genre(TypedDict):
    id: int


class Tag(TypedDict):
    id: int


@dataclass
class NovelDTO:
    title: str
    tags: list[Tag]
    genres: list[Genre]
