from pydantic import BaseModel
from uuid import UUID
from app.schemas.experienceData import experienceDataResponse

class workExperienceCreate(BaseModel):
    id_pro: UUID
    id_experience_data: UUID
   
class workExperienceResponse(BaseModel):
    
    experience: experienceDataResponse
    
    class Config:
        from_attributes = True