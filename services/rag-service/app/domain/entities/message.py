from uuid import UUID
from datetime import datetime
from typing import Optional

class Message:

    def __init__(
            self, 
            id_meesage: UUID,
            session_id: UUID,
            sender: str,
            message: str,
            emotion_tag: str,
            created_at: Optional[datetime] = None,
            ):
        
        self.id_message = id_meesage
        self.session_id = session_id
        self.sender = sender
        self.message = message
        self.emotion_tag = emotion_tag
        self.created_at = created_at