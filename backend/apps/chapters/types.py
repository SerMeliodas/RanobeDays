from pydantic import BaseModel


class ChapterObject(BaseModel):
    title: str
    novel: int  # novel id
    text: str
