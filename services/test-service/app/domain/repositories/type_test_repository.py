from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from app.domain.entities.type_test import TypeTestEntity


class ITypeTestRepository(ABC):
    """Interfaz para el repositorio de TypeTest"""

    @abstractmethod
    async def create(self, entity: TypeTestEntity) -> TypeTestEntity:
        """Crea un nuevo tipo de test"""
        pass

    @abstractmethod
    async def get_by_id(self, typeT_id: UUID) -> Optional[TypeTestEntity]:
        """Obtiene un tipo de test por su ID"""
        pass

    @abstractmethod
    async def get_all(self) -> List[TypeTestEntity]:
        """Obtiene todos los tipos de test"""
        pass

    @abstractmethod
    async def update(self, entity: TypeTestEntity) -> TypeTestEntity:
        """Actualiza un tipo de test"""
        pass

    @abstractmethod
    async def delete(self, typeT_id: UUID) -> bool:
        """Elimina un tipo de test"""
        pass
