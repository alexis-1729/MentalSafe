from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Chat:
    id: Optional[int]
    user_id: int
    message: str
    response: str
    intent: Optional[str]
    created_at: Optional[datetime] = None