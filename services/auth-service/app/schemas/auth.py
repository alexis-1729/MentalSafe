from pydantic import BaseModel, UUID4
import uuid

class LoginForm(BaseModel):
    username: str
    role: str
    password: str

class Token (BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class UserAuthUpdate(BaseModel):
    username: str | None 
    password: str | None

class UserAuthRegister(LoginForm):
    pass

class TokenData(BaseModel):
    sub: str | None = None
    role: str | None = None

class CurrentUser(BaseModel):
    userid: str
    role: str
