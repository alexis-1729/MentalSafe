from abc import ABC, abstractmethod
from app.domain.entities.message import Message
from uuid import UUID
class MessageRepository(ABC):

    @abstractmethod
    async def add(self,message: Message)-> None:
        pass

    @abstractmethod
    async def get_by_session(self, session_id: UUID)-> list[Message] | None:
        pass 