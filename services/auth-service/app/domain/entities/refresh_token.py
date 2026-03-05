from uuid import UUID
from datetime import datetime

class RefreshToken:

    def __init__(
        self,
        id:UUID,
        auth_id: UUID,
        token_hash: str,
        expires_at: datetime,
        revoked: bool = False
        ):
            self.id = id
            self.auth_id = auth_id
            self.token_hash = token_hash
            self.expires_at = expires_at
            self.revoked = revoked

    def revoke(self):
          self.revoked = True

    def is_expired(self):
          return datetime.utcnow() > self.expires_at            
