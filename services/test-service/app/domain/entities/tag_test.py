from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class TagTestEntity:
    """Entidad que representa una etiqueta de test"""
    tag_id: UUID
    name: str
    id_test_type: UUID
    type: Optional['TypeTestEntity'] = None

    class Config:
        arbitrary_types_allowed = True
