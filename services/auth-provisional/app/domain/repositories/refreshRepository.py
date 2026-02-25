from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.refresh_token import RefreshToken

class RefreshTokenRepository(ABC):

    @abstractmethod
    async def add(self, token: RefreshToken)-> None:
        pass

    @abstractmethod
    async def get_by_hash(self, token_hash: str)-> RefreshToken | None:
        pass

    @abstractmethod
    async def revoke(self, token_id: UUID)-> None:
        pass