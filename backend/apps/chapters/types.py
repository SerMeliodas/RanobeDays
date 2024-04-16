from pydantic import BaseModel


class ChapterObject(BaseModel):
    title: str | None = None
    novel: int | None = None  # novel id
    text: str | None = None
