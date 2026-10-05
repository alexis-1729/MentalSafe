from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from app.domain.repositories.sessionRepository import SessionRepository
from app.domain.entities.session import Session
from app.infraestructure.db.models.sessionModel import SessionORM
from app.infraestructure.db.mappers.sessionMapper import SessionMapper
from uuid import UUID

class SQLAlchemySessionRepository(SessionRepository):
    """Implementación del repositorio de sesiones usando SQLAlchemy"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.mapper = SessionMapper()

    async def add(self, session: Session) -> None:
        """Añadir una nueva sesión a la base de datos"""
        session_orm = self.mapper.to_orm(session)
        self.session.add(session_orm)
        await self.session.flush()

    async def get(self, user_id: UUID) -> Session | None:
        """Obtener una sesión - Implementa la interfaz del dominio"""
        
        stmt = select(SessionORM).where(SessionORM.user_id == user_id)
        result = await self.session.execute(stmt)
        session_orm = result.scalar_one_or_none()
        
        if not session_orm:
            return None
        
        return self.mapper.to_domain(session_orm)
