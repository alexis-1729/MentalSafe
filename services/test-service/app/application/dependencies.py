from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
# Importamos get_async_session desde su nueva ubicación
from app.infrastructure.db.database import get_async_session
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services.test_user_service import TestUserService
from app.application.services.type_test_service import TypeTestService

# Inyectamos el Unit of Work
async def get_unit_of_work(session: AsyncSession = Depends(get_async_session)):
    return UnitOfWorkImpl(session)

# Inyectamos el Servicio de Usuarios-Test
async def get_test_user_service(uow: UnitOfWorkImpl = Depends(get_unit_of_work)):
    return TestUserService(uow)

# Inyectamos el Servicio de Tipos de Test (por si necesitas crear nuevos tests)
async def get_type_test_service(uow: UnitOfWorkImpl = Depends(get_unit_of_work)):
    return TypeTestService(uow)