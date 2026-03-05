from abc import ABC, abstractmethod
from app.domain.entities.content import Content
from uuid import UUID

class ContentRepository(ABC):

    @abstractmethod
    async def add(self, content: Content) -> None:
        """Agregar un nuevo contenido"""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Content | None:
        """Obtener un contenido por ID"""
        pass

    @abstractmethod
    async def get_by_chapter(self, id_chapter: UUID) -> list[Content]:
        """Obtener todos los contenidos de un capítulo"""
        pass

    @abstractmethod
    async def get_all(self) -> list[Content]:
        """Obtener todos los contenidos"""
        pass