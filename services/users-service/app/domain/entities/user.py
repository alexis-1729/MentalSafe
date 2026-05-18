from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from datetime import datetime

@dataclass
class User:
    id: Optional[UUID]
    id_auth: UUID
    full_name: str
    apellidos: str
    fecha_nac: object
    genero: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
