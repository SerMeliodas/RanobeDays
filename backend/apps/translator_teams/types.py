from pydantic import BaseModel


class TranslatorTeamObject(BaseModel):
    id: None | int = None
    name: str
    users: list[int]
    novels: list[int]
