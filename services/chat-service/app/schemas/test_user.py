from pydantic import BaseModel, UUID4
from typing import Optional
from app.schemas.result_test import result_test_response
from datetime import datetime
import  uuid

class test_user_create(BaseModel):
    id_user:UUID4
    result_id: UUID4

class test_user_response(BaseModel):
    test_id: UUID4
    id_user: UUID4
    result_id: UUID4
    created_at: datetime

    result: Optional[result_test_response] = None

    class Config:
        from_attributes = True
