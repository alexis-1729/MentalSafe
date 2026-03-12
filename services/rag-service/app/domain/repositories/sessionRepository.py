from abc import ABC, abstractmethod
from app.domain.entities.session import Session
from uuid import UUID

class SessionRepository(ABC):

    @abstractmethod
    async def add(self, session: Session)-> None:
        pass

    @abstractmethod
    async def get(self, user_id: UUID)-> Session | None:
        pass