from pydantic import BaseModel, UUID4
from uuid import UUID


class speciallityCreate(BaseModel):
    name: str
    description: str

class speciallityResponse(BaseModel):
    id_speciallity: UUID
    name: str
    description: str

    class Config:
        from_attributes = True

