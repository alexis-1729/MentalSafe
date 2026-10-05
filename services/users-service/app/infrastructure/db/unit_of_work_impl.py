from app.infrastructure.db.database import AsyncSessionLocal
from app.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl

class UnitOfWorkImpl:
    def __init__(self):
        self.session_factory = AsyncSessionLocal
        self.session = None

    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = UserRepositoryImpl(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                await self.session.commit()  
            else:
                await self.session.rollback() 
        finally:
            await self.session.close()       