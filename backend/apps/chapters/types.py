from pydantic import BaseModel


class ChapterDTO(BaseModel):
    title: str
    novel: int  # novel id
    text: str
