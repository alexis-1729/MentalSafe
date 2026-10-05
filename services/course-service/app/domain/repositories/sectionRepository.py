from abc import ABC, abstractmethod
from app.domain.entities.section import Section
from uuid import UUID


class SectionRepository(ABC):

    @abstractmethod
    async def add(self, section: Section) -> None:
        """Agregar una nueva sección"""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Section | None:
        """Obtener una sección por ID"""
        pass

    @abstractmethod
    async def get_by_course(self, id_course: UUID) -> list[Section]:
        """Obtener todas las secciones de un curso"""
        pass

    @abstractmethod
    async def get_all(self) -> list[Section]:
        """Obtener todas las secciones"""
        pass