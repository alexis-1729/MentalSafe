from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class ChatMessageCreate(BaseModel):
    session_id: UUID
    sender: str
    message: str
    emotion_tag: str
    created_at: datetime

    class Config:
        orm_mode = True

class ChatMessageResponse(BaseModel):
    id_message: UUID
    session_id: UUID
    sender: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True