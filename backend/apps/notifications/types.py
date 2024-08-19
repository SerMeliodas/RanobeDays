from pydantic import BaseModel


class NotificationObject(BaseModel):
    notification_type: str | None = None
    novel: str | None = None
    users: list[int] | None = None
    message: str | None = None
