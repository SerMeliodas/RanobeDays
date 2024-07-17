from pydantic import BaseModel


class ChapterObject(BaseModel):
    title: str | None = None
    novel: int | None = None  # novel id
    volume: int | None = None
    number: int | None = None
    team: int | None = None
    text: str | None = None
