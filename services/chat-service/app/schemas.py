from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID

class type_test_create(BaseModel):
    name_test: str
    num_q: int

class type_test_response(BaseModel):
    typeT_id: UUID
    name_test: str
    num_q: int

    class Config:
        orm_mode = True

class tags_test_create(BaseModel):
    id_test_type: UUID
    name: str

class tags_test_response(BaseModel):
    tag_id: UUID
    name: str
    id_test_type: UUID

    type: Optional[type_test_response] = None

    class Config:
        orm_mode = True

class result_test_create(BaseModel):
    score:int
    id_tag: UUID

class result_test_response(BaseModel):
    result_id: UUID
    socre:int
    id_tag:UUID

    tag: Optional[tags_test_response] = None
    
    class Config:
        orm_mode = True

class test_user_create(BaseModel):
    id_user:UUID
    result_id: UUID

class test_user_response(BaseModel):
    test_id: UUID
    id_user: UUID
    result_id: UUID
    created_at: datetime

    result = Optional[result_test_response] = None

    class Config:
        orm_mode = True


class MessageRequest(BaseModel):
    session_id: str
    message: str
    language_code: str = "es"  

