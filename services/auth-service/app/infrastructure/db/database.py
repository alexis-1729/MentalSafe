from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from app.infrastructure.config import Settings
import os


load_dotenv()



engine = create_async_engine(
    Settings.DB_URL,
    echo = False,
    pool_pre_ping = True
)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit = False, class_ = AsyncSession)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()