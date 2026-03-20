from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from app.domain.entities.test_user import TestUserEntity


class ITestUserRepository(ABC):
    """Interfaz para el repositorio de TestUser"""

    @abstractmethod
    async def create(self, entity: TestUserEntity) -> TestUserEntity:
        """Crea una nueva relación usuario-test"""
        pass

    @abstractmethod
    async def get_by_id(self, test_id: UUID) -> Optional[TestUserEntity]:
        """Obtiene una relación usuario-test por su ID"""
        pass

    @abstractmethod
    async def get_all(self) -> List[TestUserEntity]:
        """Obtiene todas las relaciones usuario-test"""
        pass

    @abstractmethod
    async def update(self, entity: TestUserEntity) -> TestUserEntity:
        """Actualiza una relación usuario-test"""
        pass

    @abstractmethod
    async def delete(self, test_id: UUID) -> bool:
        """Elimina una relación usuario-test"""
        pass

    @abstractmethod
    async def get_by_user_id(self, id_user: UUID) -> List[TestUserEntity]:
        """Obtiene todos los tests de un usuario específico"""
        pass

    @abstractmethod
    async def get_by_result_id(self, result_id: UUID) -> List[TestUserEntity]:
        """Obtiene todas las relaciones usuario-test de un resultado específico"""
        pass
