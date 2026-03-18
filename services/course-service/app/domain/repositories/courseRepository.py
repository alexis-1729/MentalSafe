from abc import ABC, abstractmethod
from app.domain.entities.course import Course
from uuid import UUID


class CourseRepository(ABC):

    @abstractmethod
    async def add(self, course: Course) -> None:
        """Agregar un nuevo curso"""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Course | None:
        """Obtener un curso por ID"""
        pass

    @abstractmethod 
    async def get_by_tag(self, tag: str) -> Course | None:
        """Obtener un curso por etiqueta"""
        pass
    
    @abstractmethod
    async def get_all(self) -> list[Course]:
        """Obtener todos los cursos"""
        pass

