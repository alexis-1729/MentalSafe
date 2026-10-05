from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
import os


load_dotenv()


DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_async_engine(
    DATABASE_URL,
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