from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.domain.repositories.courseRepository import CourseRepository
from app.domain.entities.course import Course
from app.infraestructure.db.mappers.courseMapper import CourseMapper
from app.infraestructure.db.models.courseModel import CourseORM
from sqlalchemy.exc import SQLAlchemyError


class SQLAlchemyCourseRepository(CourseRepository):
    """Implementación concreta del repositorio de cursos usando SQLAlchemy async"""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def add(self, course: Course) -> None:
        """
        Agrega un nuevo curso a la base de datos
        
        Args:
            course: Entidad de dominio Course que será persistida
            
        Raises:
            RuntimeError: Si ocurre un error en la base de datos
        """
        try:
            orm_course = CourseMapper.to_orm(course)
            self.session.add(orm_course)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error al agregar curso: {str(e.orig)}")
    
    async def get_by_id(self, id: UUID) -> Course | None:
        """
        Obtiene un curso por su ID
        
        Args:
            id: UUID del curso a buscar
            
        Returns:
            Course: Entidad de dominio si existe, None en caso contrario
        """
        try:
            query = select(CourseORM).where(CourseORM.id_course == id)
            result = await self.session.execute(query)
            course_model = result.scalar_one_or_none()
            
            if course_model is None:
                return None
            
            return course_model.to_entity()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener curso por ID: {str(e.orig)}")
    
    async def get_by_tag(self, tag: str) -> Course | None:
        """
        Obtiene un curso por su etiqueta (tag)
        
        Args:
            tag: Etiqueta del curso a buscar
            
        Returns:
            Course: Entidad de dominio si existe, None en caso contrario
        """
        try:
            query = select(CourseORM).where(CourseORM.tag == tag)
            result = await self.session.execute(query)
            course_model = result.scalar_one_or_none()
            
            if course_model is None:
                return None
            
            return course_model.to_entity()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener curso por tag: {str(e.orig)}")
    
    async def get_all(self) -> list[Course]:
        """
        Obtiene todos los cursos
        
        Returns:
            list[Course]: Lista de entidades de dominio Course
        """
        try:
            query = select(CourseORM)
            result = await self.session.execute(query)
            course_models = result.scalars().all()
            
            return [course_model.to_entity() for course_model in course_models]
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener cursos: {str(e.orig)}")
