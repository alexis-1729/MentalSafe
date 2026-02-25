from pydantic import BaseModel
from uuid import UUID

class UserCreate(BaseModel):
    email: str
    password_h: str
    role: str

class UserResponse(BaseModel):
    id: UUID
    email: str
    role: str

class UserLogin(BaseModel):
    email: str
    password_h: str