from pydantic import BaseModel, UUID4
from uuid import UUID
from app.schemas.section import sectionResponse

class  courseCreate(BaseModel):
    title: str
    description: str
    tag: str
    url_image: str

class courseResponse(BaseModel):
    id_course: UUID
    title: str
    description: str
    tag : str
    url_image: str
    # section: sectionResponse

    class Config: 
        from_atributes = True

# class courseCompleteResponse(BaseModel):
#     info_curso: courseResponse
    

