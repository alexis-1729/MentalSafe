from pydantic import BaseModel, UUID4
from enum import Enum
from typing import Optional
from datetime import datetime

class ChatSessionCreate(BaseModel):
    user_id: UUID4
    title:Optional[str] = None

class ChatSessionResponse(BaseModel):
    session_id: UUID4
    created_at: datetime

class ChatMessageCreate(BaseModel):
    sender: str
    content: str

class ChatMessageResponse(BaseModel):
    id_message: UUID
    session_id: UUID
    sender: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True
