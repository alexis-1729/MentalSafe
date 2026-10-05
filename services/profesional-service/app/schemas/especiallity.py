from pydantic import BaseModel, UUID4
from app.schemas.especiallityData import speciallityResponse
from uuid import UUID

class profesionSpCreate(BaseModel):
    id_pro: UUID
    id_speciallity: UUID
   

class profesionalSpResponse(BaseModel):
    id_proEsp: UUID
    speciallity: list[speciallityResponse]
   
    class Config:
        from_attributes=True