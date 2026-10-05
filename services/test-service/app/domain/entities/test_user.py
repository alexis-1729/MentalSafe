from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from datetime import datetime


@dataclass
class TestUserEntity:
    """Entidad que representa la relación entre un usuario y un test"""
    test_id: UUID
    id_user: UUID
    result_id: UUID
    created_at: datetime
    result: Optional['ResultTestEntity'] = None

    class Config:
        arbitrary_types_allowed = True
