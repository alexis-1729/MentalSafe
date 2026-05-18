from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repositories.authRepository import AuthRepository
from app.domain.entities.auth import Auth
from app.domain.exceptions import UserAlredyExists
from app.infrastructure.db.models.authModel import AuthORM
from app.infrastructure.db.mappers.authMapper import AuthMapper



class SQLAlchemyAuthRepository(AuthRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, auth: Auth)-> None:
        try:
            orm_auth = AuthMapper.to_orm(auth)
            self.session.add(orm_auth)
            await self.session.flush()
        except IntegrityError:
            raise UserAlredyExists()
    
    async def get(self, email: str):
        stmt = select(AuthORM).where(AuthORM.email == email)
        result = await self.session.execute(stmt)
        orm_auth = result.scalars().first()

        if orm_auth is None :
            return None
        return AuthMapper.to_domain(orm_auth)