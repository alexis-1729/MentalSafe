from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services import (
    TypeTestService,
    ResultTestService,
    TagTestService,
    TestUserService,
)
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de la base de datos asíncrona
DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False,
)


async def get_async_session() -> AsyncSession:
    """Obtiene una sesión asíncrona"""
    async with AsyncSessionLocal() as session:
        yield session


async def get_unit_of_work(session: AsyncSession = Depends(get_async_session)) -> UnitOfWorkImpl:
    """Obtiene el Unit of Work"""
    return UnitOfWorkImpl(session)


async def get_type_test_service(
    uow: UnitOfWorkImpl = Depends(get_unit_of_work),
) -> TypeTestService:
    """Inyecta el servicio de TypeTest"""
    return TypeTestService(uow)


async def get_result_test_service(
    uow: UnitOfWorkImpl = Depends(get_unit_of_work),
) -> ResultTestService:
    """Inyecta el servicio de ResultTest"""
    return ResultTestService(uow)


async def get_tag_test_service(
    uow: UnitOfWorkImpl = Depends(get_unit_of_work),
) -> TagTestService:
    """Inyecta el servicio de TagTest"""
    return TagTestService(uow)


async def get_test_user_service(
    uow: UnitOfWorkImpl = Depends(get_unit_of_work),
) -> TestUserService:
    """Inyecta el servicio de TestUser"""
    return TestUserService(uow)
