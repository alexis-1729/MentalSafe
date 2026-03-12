from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional

class ChatSessionCreate(BaseModel):
    user_id: UUID
    title:Optional[str] = None

class ChatSessionResponse(BaseModel):
    session_id: UUID
    created_at: datetime
    updated_at: datetime
