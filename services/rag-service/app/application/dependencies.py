from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infraestructure.database import get_db
from app.infraestructure.db.unit_of_work import SQLAlchemyUnitOfWork
from app.domain.unit_of_work import UnitOfWork
from app.application.services.messageService import MessageService
from app.application.services.sessionService import SessionService
from app.application.pipeline.flow import Pipeline

# Dependencia para UoW
async def get_uow_dependency(
    session: AsyncSession = Depends(get_db)
) -> UnitOfWork:
    """Obtener una instancia del Unit of Work"""
    return SQLAlchemyUnitOfWork(session)


# Dependencias para Services
async def get_message_service(
    uow: UnitOfWork = Depends(get_uow_dependency)
) -> MessageService:
    """Obtener instancia del servicio de mensajes"""
    return MessageService(uow)


async def get_session_service(
    uow: UnitOfWork = Depends(get_uow_dependency)
) -> SessionService:
    """Obtener instancia del servicio de sesiones"""
    return SessionService(uow)

async def get_pipeline()->Pipeline:
    return Pipeline("Mental")