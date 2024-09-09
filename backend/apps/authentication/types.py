from pydantic import BaseModel


class RegisterObject(BaseModel):
    email: str
    username: str
    public_username: str
    password1: str
    password2: str


class LoginObject(BaseModel):
    email: str
    password: str


class VerifyEmailObject(BaseModel):
    token: str


class SendVerificationEmailObject(BaseModel):
    email: str
