from pydantic import BaseModel


class NovelObject(BaseModel):
    title: str | None = None
    original_title: str | None = None

    language: int | None = None
    translate_language: int | None = None

    status: int | None = None

    country: int | None = None
    tags: list[int] | None = None
    genres: list[int] | None = None

    synopsys: str | None = None
