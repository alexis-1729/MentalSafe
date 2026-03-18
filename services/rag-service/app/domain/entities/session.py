from uuid import UUID
from datetime import datetime
from typing import Optional

class Session:

    def __init__(
            self,
            user_id: UUID,
            title: str,
            id_session: Optional[UUID] = None,
            created_at: Optional[datetime] = None,
            updated_at: Optional[datetime] = None,
            ):
        self.id_session = id_session
        self.user_id = user_id
        self.title = title
        self.created_at = created_at
        self.updated_at = updated_at
        