from app.domain.unit_of_work import AbstractUnitOfWork
from app.infrastructure.db.repositories.auth_repository import SQLAlchemyAuthRepository
from app.infrastructure.db.repositories.refreshTokenRepository import SQLAlchemyRefreshTokenRepository
class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.auth = SQLAlchemyAuthRepository(self.session)
        self.refresh_tokens = SQLAlchemyRefreshTokenRepository(self.session)
        return await super().__aenter__()
    
    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session().rollback()