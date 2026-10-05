from pydantic import BaseModel, UUID4
from typing import Optional
from app.schemas.experienceData import experienceDataResponse
from app.schemas.especiallityData import speciallityResponse
from uuid import UUID
class profesionalCreate(BaseModel):
    name: str
    apellido_pa: str
    apellido_ma: str
    email: str
    country: str
    city: str
    id_profesional: UUID
    
class profesionalResponse(BaseModel):
    name: str
    apellido_pa: str
    apellido_ma: str
    email: str
    country: str
    city: str
    certification: str

    class Config:
        from_attributes = True

class startPoint(BaseModel):
    id_pro: UUID
    level: str
    
class startPointResponse(BaseModel):
    five : int
    four: int
    three: int
    two: int
    one: int
    media: float

#Negocio
class profesionalCompleteResponse(BaseModel):
    perfil: profesionalResponse
    workExperience: list[experienceDataResponse]
    speciallity: list[speciallityResponse]
    calification: startPointResponse
    
    class Config:
        from_attributes= True




