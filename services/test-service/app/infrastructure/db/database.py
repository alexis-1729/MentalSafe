from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Base para los modelos
Base = declarative_base()

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