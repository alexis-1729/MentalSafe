from pydantic import BaseModel, UUID4
from typing import Optional, List
from datetime import datetime

# Schema para Tipo de Test
class TypeTestBase(BaseModel):
    name_test: str
    num_q: int

class TypeTestResponse(TypeTestBase):
    typeT_id: UUID4
    class Config:
        from_attributes = True

# Schema para Resultados
class ResultTestCreate(BaseModel):
    score: int
    id_test: UUID4

class ResultTestResponse(BaseModel):
    result_id: UUID4
    score: int
    id_test: UUID4
    class Config:
        from_attributes = True

# Schema para Test User (El que registra que un usuario hizo un test)
class TestUserCreate(BaseModel):
    id_user: UUID4
    result_id: UUID4

class TestUserResponse(BaseModel):
    test_id: UUID4
    id_user: UUID4
    result_id: UUID4
    created_at: datetime
    class Config:
        from_attributes = True