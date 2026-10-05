from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.unit_of_work import UnitOfWork
from app.infraestructure.db.repositories.messageRepository import SQLAlchemyMessageRepository
from app.infraestructure.db.repositories.sessionRepository import SQLAlchemySessionRepository


class SQLAlchemyUnitOfWork(UnitOfWork):
    """Implementación del Unit of Work para SQLAlchemy"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.messages = SQLAlchemyMessageRepository(session)
        self.sessions = SQLAlchemySessionRepository(session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self) -> None:
        """Confirmar todos los cambios"""
        await self.session.commit()

    async def rollback(self) -> None:
        """Deshacer todos los cambios"""
        await self.session.rollback()
