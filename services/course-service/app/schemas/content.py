from pydantic import BaseModel, UUID4
from typing import Optional
from uuid import UUID

class contentCreate(BaseModel):
    content: str
    url_video: str
    id_chap: UUID

class contentResponse(BaseModel):
    id_content: UUID
    content: str
    url_video: str
    complete: bool
    class Config:
        from_atributes = True