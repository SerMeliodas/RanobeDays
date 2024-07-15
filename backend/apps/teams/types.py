from pydantic import BaseModel


class TeamObject(BaseModel):
    id: int | None = None
    name: str | None = None
    users: list[int] | None = None
    novels: list[int] | None = None
