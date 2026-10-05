from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://alexis1729:Singer22jkM@usersdb:5432/usersdb")

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()