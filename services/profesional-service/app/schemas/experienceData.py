from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class experienceDataCreate(BaseModel):
    companyInst: str
    position: str
    sector: str
    description: str
    start_date: datetime
    finish_date: datetime

class experienceDataResponse(BaseModel):
    id_data: UUID
    companyInst: str
    position: str
    sector: str
    description: str
    start_date: datetime
    finish_date: datetime

    class Config:
        from_attributes = True


