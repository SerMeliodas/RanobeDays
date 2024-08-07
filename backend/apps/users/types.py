from pydantic import BaseModel


class UserObject(BaseModel):
    public_username: str | None = None
    email: str | None = None
    username: str | None = None
    password: str | None = None


class UserNewPassObject(BaseModel):
    old_password: str | None = None
    new_password1: str | None = None
    new_password2: str | None = None
