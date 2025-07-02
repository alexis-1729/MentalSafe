from pydantic import BaseModel, UUID4
import uuid

class LoginForm(BaseModel):
    username: str
    password: str

class Token (BaseModel):
    access_token: str
    token_type: str

    