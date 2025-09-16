from pydantic import BaseModel, UUID4
from uuid import UUID
from app.schemas.content import contentResponse

class chapterCreate(BaseModel):
    title: str
    description: str
    num_caps: str
    duration: str
    numero: int
    complete: bool
    id_sect: UUID
    url_image: str

class chapterResponse(BaseModel):
    id_chapter: UUID
    title: str
    description: str
    duration: str
    numero: int
    complete: bool
    url_image: str

    class Config: 
        from_atributes =  True
