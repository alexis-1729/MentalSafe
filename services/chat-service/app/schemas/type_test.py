from pydantic import BaseModel, UUID4
import uuid

class type_test_create(BaseModel):
    name_test: str
    num_q: int

class type_test_response(BaseModel):
    typeT_id: UUID4
    name_test: str
    num_q: int

    class Config:
        from_attributes = True