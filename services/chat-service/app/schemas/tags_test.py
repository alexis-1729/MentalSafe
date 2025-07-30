from pydantic import BaseModel, UUID4
from typing import Optional
from app.schemas.type_test import type_test_response
import uuid

class tags_test_create(BaseModel):
    id_test_type: UUID4
    name: str

class tags_test_response(BaseModel):
    tag_id: UUID4
    name: str
    id_test_type: UUID4

    type: Optional[type_test_response] = None

    class Config:
        from_attributes = True