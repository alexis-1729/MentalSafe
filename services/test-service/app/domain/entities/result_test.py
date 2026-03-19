from dataclasses import dataclass
from typing import Optional, List
from uuid import UUID


@dataclass
class ResultTestEntity:
    """Entidad que representa un resultado de test"""
    result_id: UUID
    score: int
    id_test: UUID
    test: Optional['TypeTestEntity'] = None
    test_users: Optional[List['TestUserEntity']] = None

    class Config:
        arbitrary_types_allowed = True
