from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from app.domain.entities.tag_test import TagTestEntity


class ITagTestRepository(ABC):
    """Interfaz para el repositorio de TagTest"""

    @abstractmethod
    async def create(self, entity: TagTestEntity) -> TagTestEntity:
        """Crea una nueva etiqueta de test"""
        pass

    @abstractmethod
    async def get_by_id(self, tag_id: UUID) -> Optional[TagTestEntity]:
        """Obtiene una etiqueta de test por su ID"""
        pass

    @abstractmethod
    async def get_all(self) -> List[TagTestEntity]:
        """Obtiene todas las etiquetas de test"""
        pass

    @abstractmethod
    async def update(self, entity: TagTestEntity) -> TagTestEntity:
        """Actualiza una etiqueta de test"""
        pass

    @abstractmethod
    async def delete(self, tag_id: UUID) -> bool:
        """Elimina una etiqueta de test"""
        pass

    @abstractmethod
    async def get_by_test_type_id(self, id_test_type: UUID) -> List[TagTestEntity]:
        """Obtiene todas las etiquetas de un tipo de test específico"""
        pass
