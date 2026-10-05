from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.auth import Auth

class AuthRepository(ABC):

    @abstractmethod
    async def add(self, auth: Auth)-> None:
        pass

    @abstractmethod
    async def get(self, email)-> Auth | None:
        pass