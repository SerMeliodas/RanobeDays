from pydantic import BaseModel
import jwt


class GoogleLoginCredentialsObject(BaseModel):
    client_id: str
    project_id: str
    secret: str


class GoogleLoginObject(BaseModel):
    code: str
    state: str
    error: str | None = None


class GoogleAccessTokensObject(BaseModel):
    id_token: str
    access_token: str

    def decode_id_token(self):
        return jwt.decode(self.id_token, options={'verify_signature': False})
