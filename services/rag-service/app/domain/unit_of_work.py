from abc import ABC, abstractmethod
from app.domain.repositories.messageRepository import MessageRepository
from app.domain.repositories.sessionRepository import SessionRepository


class UnitOfWork(ABC):
    """Patrón Unit of Work para coordinar cambios de repositorios"""

    messages: MessageRepository
    sessions: SessionRepository

    @abstractmethod
    async def __aenter__(self):
        return self

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    async def commit(self) -> None:
        """Confirmar todos los cambios realizados"""
        pass

    @abstractmethod
    async def rollback(self) -> None:
        """Rollback de todos los cambios realizados"""
        pass
