from pydantic import BaseModel


class TagObject(BaseModel):
    id: int | None = None
    name: str | None = None


class GenreObject(BaseModel):
    id: int | None = None
    name: str | None = None


class LanguageObject(BaseModel):
    id: int | None = None
    name: str | None = None
    abbreviation: str | None = None


class CountryObject(BaseModel):
    id: int | None = None
    name: str | None = None
