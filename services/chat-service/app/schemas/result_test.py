from pydantic import BaseModel, UUID4
from typing import Optional
from app.schemas.tags_test import tags_test_response
import uuid

class result_test_create(BaseModel):
    score:int
    id_test: UUID4

class result_test_response(BaseModel):
    result_id: UUID4
    score:int
    id_test:UUID4

    tag: Optional[tags_test_response] = None
    
    class Config:
        from_attributes= True

class ScoreResponse(BaseModel):
    status: str
    score: int | None
    description: str

