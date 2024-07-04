from pydantic import BaseModel


class ChapterObject(BaseModel):
    title: str | None = None
    novel: int | None = None  # novel id
    translator_team: int | None = None
    text: str | None = None
