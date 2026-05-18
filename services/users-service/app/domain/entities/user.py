from dataclasses import dataclass
from uuid import UUID
from typing import Optional

@dataclass
class User:
    id: Optional[UUID]
    name: str
    last_name: str
