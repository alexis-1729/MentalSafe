from pydantic import BaseModel
from uuid import UUID


class courseCreate(BaseModel):
    title: str
    description: str
    tag: str
    url_image: str

class courseResponse(BaseModel):
    id_course: UUID
    title: str
    description: str
    tag: str
    url_image: str