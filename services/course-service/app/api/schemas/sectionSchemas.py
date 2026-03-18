from pydantic import BaseModel, UUID4
from typing import Optional
from uuid import UUID

class sectionCreate(BaseModel):
    id_cours: UUID

class sectionResponse(BaseModel):
    id_section: UUID
    id_cours:UUID
    class Config: 
        from_atributes = True
