from dataclasses import dataclass
from typing import Optional, List
from uuid import UUID


@dataclass
class TypeTestEntity:
    """Entidad que representa un tipo de test"""
    typeT_id: UUID
    name_test: str
    num_q: int
    results: Optional[List['ResultTestEntity']] = None
    tags: Optional[List['TagTestEntity']] = None

    class Config:
        arbitrary_types_allowed = True
