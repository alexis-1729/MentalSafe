from abc import ABC, abstractmethod
from app.domain.entities.chapter import Chapter
from uuid import UUID

class ChapterRepository(ABC):

    @abstractmethod
    async def add(self, chapter: Chapter) -> None:
        """Agregar nuevo capítulo"""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Chapter | None:
        """Obtener un capítulo por ID"""
        pass

    @abstractmethod
    async def get_list_chapter(self, id_course: UUID) -> list[Chapter]:
        """Obtener lista de capítulos por id course"""
        pass

    @abstractmethod
    async def get_all(self) -> list[Chapter]:
        """Obtener todos los capítulos"""
        pass