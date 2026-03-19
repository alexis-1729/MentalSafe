from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.unit_of_work import AbstractUnitOfWork
from app.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl

class UnitOfWorkImpl(AbstractUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.users = UserRepositoryImpl(session)

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()