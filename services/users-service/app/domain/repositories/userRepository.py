from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from app.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> None:
        """Agregar un nuevo usuario"""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[User]:
        """Obtener un usuario por ID"""
        pass

    @abstractmethod
    async def get_by_id_auth(self, id_auth: UUID) -> Optional[User]:
        """Obtener un usuario por ID de autenticación"""
        pass

    @abstractmethod
    async def get_all(self) -> list[User]:
        """Obtener todos los usuarios"""
        pass