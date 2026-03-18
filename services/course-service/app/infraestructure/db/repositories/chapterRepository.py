from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.domain.repositories.chapterRepository import ChapterRepository
from app.domain.entities.chapter import Chapter
from app.infraestructure.db.mappers.chapterMapper import ChapterMapper
from app.infraestructure.db.models.chapterModel import ChapterORM
from sqlalchemy.exc import SQLAlchemyError

class SQLAlchemyChapterRepository(ChapterRepository):
    """Implementación concreta del repositorio de capítulos usando SQLAlchemy async"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, chapter: Chapter) -> None:
        """
        Agrega un nuevo capítulo a la base de datos
        
        Args:
            chapter: Entidad de dominio Chapter que será persistida
            
        Raises:
            RuntimeError: Si ocurre un error en la base de datos
        """
        try:
            orm_chapter = ChapterMapper.to_orm(chapter)
            self.session.add(orm_chapter)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error al agregar capítulo: {str(e.orig)}")

    async def get_by_id(self, id: UUID) -> Chapter | None:
        """
        Obtiene un capítulo por su ID
        
        Args:
            id: UUID del capítulo a buscar
            
        Returns:
            Chapter: Entidad de dominio si existe, None en caso contrario
        """
        try:
            query = select(ChapterORM).where(ChapterORM.id_chapter == id)
            result = await self.session.execute(query)
            chapter_model = result.scalar_one_or_none()
            
            if chapter_model is None:
                return None
            
            return ChapterMapper.to_domain(chapter_model)
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener capítulo por ID: {str(e.orig)}")

    async def get_list_chapter(self, id_course: UUID) -> list[Chapter]:
        """
        Obtiene lista de capítulos por id curso
        
        Args:
            id_course: UUID del curso
            
        Returns:
            list[Chapter]: Lista de entidades de dominio Chapter
        """
        try:
            query = select(ChapterORM).where(ChapterORM.id_course == id_course)
            result = await self.session.execute(query)
            chapters = result.scalars().all()
            
            return [ChapterMapper.to_domain(chapter) for chapter in chapters]
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener capítulos: {str(e.orig)}")

    async def get_all(self) -> list[Chapter]:
        """
        Obtiene todos los capítulos
        
        Returns:
            list[Chapter]: Lista de entidades de dominio Chapter
        """
        try:
            query = select(ChapterORM)
            result = await self.session.execute(query)
            chapters = result.scalars().all()
            
            return [ChapterMapper.to_domain(chapter) for chapter in chapters]
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error al obtener capítulos: {str(e.orig)}")