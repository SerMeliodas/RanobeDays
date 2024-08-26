from pydantic import BaseModel


class NovelObject(BaseModel):
    title: str | None = None
    creator: int | None = None
    original_title: str | None = None

    language: int | None = None
    translated_language: int | None = None

    status: str | None = None

    country: int | None = None
    tags: list[int] | None = None
    genres: list[int] | None = None

    synopsys: str | None = None
