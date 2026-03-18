from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    password: str
    full_name: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None