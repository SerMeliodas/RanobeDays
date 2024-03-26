from pydantic import BaseModel


class TranslatorTeamDTO(BaseModel):
    id: None | int = None
    name: str
    users: list[int]
    novels: list[int]
