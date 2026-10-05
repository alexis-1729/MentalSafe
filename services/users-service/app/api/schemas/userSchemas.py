from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import Optional

class UserCreate(BaseModel):
    id_auth: UUID 
    full_name: str
    apellidos: str
    fecha_nac: date
    genero: str

class UserResponse(BaseModel):
    id: UUID
    id_auth: UUID
    full_name: str
    apellidos: str
    fecha_nac: date
    genero: str

    class Config:
        from_attributes = True