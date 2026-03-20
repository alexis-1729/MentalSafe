
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DB_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

class TestSettings:
    DB_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:{os.getenv('DB_TEST_PORT')}/{os.getenv('DB_TEST')}"
