from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.domain.entities.section import Section
from app.domain.repositories.sectionRepository import SectionRepository
from app.infraestructure.db.mappers.sectionMapper import SectionMapper
from app.infraestructure.db.models.sectionModel import SectionORM
from sqlalchemy.exc import SQLAlchemyError

class SQLAlchemySectionRepository(SectionRepository):
    """Implementación concreta del repositorio de secciones usando SQLAlchemy async"""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, section: Section) -> None:
        """
        Agrega una nueva sección a la base de datos
        
        Args:
            section: Entidad de dominio Section que será persistida
            
        Raises:
            RuntimeError: Si ocurre un error en la base de datos
        """
        try:
            orm_section = SectionMapper.to_orm(section)
            self.session.add(orm_section)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error al agregar sección: {str(e.orig)}")

    async def get_by_id(self, id: UUID) -> Section | None:
        """
        Obtiene una sección por su ID
        
        Args:
            id: UUID de la sección a buscar
            
        Returns:
            Section: Entidad de dominio si existe, None en caso contrario
        """
        try:
            query = select(SectionORM).where(SectionORM.id_section == id)
            result = await self.session.execute(query)
            section_model = result.scalar_one_or_none()
            
            if section_model is None:
                return None
            
            return SectionMapper.to_domain(section_model)
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener sección por ID: {str(e.orig)}")

    async def get_by_course(self, id_course: UUID) -> list[Section]:
        """
        Obtiene todas las secciones de un curso
        
        Args:
            id_course: UUID del curso
            
        Returns:
            list[Section]: Lista de entidades de dominio Section
        """
        try:
            query = select(SectionORM).where(SectionORM.id_course == id_course)
            result = await self.session.execute(query)
            section_models = result.scalars().all()
            
            return [SectionMapper.to_domain(section_model) for section_model in section_models]
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener secciones por curso: {str(e.orig)}")

    async def get_all(self) -> list[Section]:
        """
        Obtiene todas las secciones
        
        Returns:
            list[Section]: Lista de entidades de dominio Section
        """
        try:
            query = select(SectionORM)
            result = await self.session.execute(query)
            section_models = result.scalars().all()
            
            return [SectionMapper.to_domain(section_model) for section_model in section_models]
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener secciones: {str(e.orig)}")