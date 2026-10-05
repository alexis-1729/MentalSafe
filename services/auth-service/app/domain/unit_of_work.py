from abc import ABC, abstractmethod
from app.domain.repositories.authRepository import AuthRepository
from app.domain.repositories.refreshRepository import RefreshTokenRepository
class AbstractUnitOfWork(ABC):
    
    auth: AuthRepository
    refresh_token: RefreshTokenRepository

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass