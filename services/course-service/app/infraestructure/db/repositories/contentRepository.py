from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.domain.entities.content import Content
from app.domain.repositories.contentRepository import ContentRepository
from app.infraestructure.db.mappers.contentMapper import ContentMapper
from app.infraestructure.db.models.contentModel import ContentORM
from sqlalchemy.exc import SQLAlchemyError


class SQLAlchemyContentRepository(ContentRepository):
    """Implementación concreta del repositorio de contenidos usando SQLAlchemy async"""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def add(self, content: Content) -> None:
        """
        Agrega un nuevo contenido a la base de datos
        
        Args:
            content: Entidad de dominio Content que será persistida
            
        Raises:
            RuntimeError: Si ocurre un error en la base de datos
        """
        try:
            orm_content = ContentMapper.to_orm(content)
            self.session.add(orm_content)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error al agregar contenido: {str(e.orig)}")
    
    async def get_by_id(self, id: UUID) -> Content | None:
        """
        Obtiene un contenido por su ID
        
        Args:
            id: UUID del contenido a buscar
            
        Returns:
            Content: Entidad de dominio si existe, None en caso contrario
        """
        try:
            query = select(ContentORM).where(ContentORM.id_content == id)
            result = await self.session.execute(query)
            content_model = result.scalar_one_or_none()
            
            if content_model is None:
                return None
            
            return ContentMapper.to_domain(content_model)
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener contenido por ID: {str(e.orig)}")
    
    async def get_by_chapter(self, id_chapter: UUID) -> list[Content]:
        """
        Obtiene todos los contenidos de un capítulo
        
        Args:
            id_chapter: UUID del capítulo
            
        Returns:
            list[Content]: Lista de entidades de dominio Content
        """
        try:
            query = select(ContentORM).where(ContentORM.id_chapter == id_chapter)
            result = await self.session.execute(query)
            content_models = result.scalars().all()
            
            return [ContentMapper.to_domain(content_model) for content_model in content_models]
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener contenidos por capítulo: {str(e.orig)}")
    
    async def get_all(self) -> list[Content]:
        """
        Obtiene todos los contenidos
        
        Returns:
            list[Content]: Lista de entidades de dominio Content
        """
        try:
            query = select(ContentORM)
            result = await self.session.execute(query)
            content_models = result.scalars().all()
            
            return [ContentMapper.to_domain(content_model) for content_model in content_models]
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener contenidos: {str(e.orig)}")