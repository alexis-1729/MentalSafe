from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from app.domain.entities.result_test import ResultTestEntity


class IResultTestRepository(ABC):
    """Interfaz para el repositorio de ResultTest"""

    @abstractmethod
    async def create(self, entity: ResultTestEntity) -> ResultTestEntity:
        """Crea un nuevo resultado de test"""
        pass

    @abstractmethod
    async def get_by_id(self, result_id: UUID) -> Optional[ResultTestEntity]:
        """Obtiene un resultado de test por su ID"""
        pass

    @abstractmethod
    async def get_all(self) -> List[ResultTestEntity]:
        """Obtiene todos los resultados de test"""
        pass

    @abstractmethod
    async def update(self, entity: ResultTestEntity) -> ResultTestEntity:
        """Actualiza un resultado de test"""
        pass

    @abstractmethod
    async def delete(self, result_id: UUID) -> bool:
        """Elimina un resultado de test"""
        pass

    @abstractmethod
    async def get_by_test_id(self, id_test: UUID) -> List[ResultTestEntity]:
        """Obtiene todos los resultados de un tipo de test específico"""
        pass
