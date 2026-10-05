from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatCreate(BaseModel):
    user_id: int
    message: str

class ChatResponse(BaseModel):
    id: int
    user_id: int
    message: str
    response: str
    intent: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True