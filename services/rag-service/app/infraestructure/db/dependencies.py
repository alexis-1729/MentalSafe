from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.infraestructure.database import get_db
from app.infraestructure.db.unit_of_work import SQLAlchemyUnitOfWork
from app.domain.unit_of_work import UnitOfWork


async def get_unit_of_work(session: AsyncSession = None) -> AsyncGenerator[UnitOfWork, None]:
    """Obtener una instancia de Unit of Work"""
    # Si no se proporciona sesión, usar la del contexto async
    if session is None:
        async for db_session in get_db():
            async with SQLAlchemyUnitOfWork(db_session) as uow:
                yield uow
    else:
        async with SQLAlchemyUnitOfWork(session) as uow:
            yield uow

