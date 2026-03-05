from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.domain.repositories.refreshRepository import RefreshTokenRepository
from app.domain.entities.refresh_token import RefreshToken
from app.domain.exceptions import RegisterNotExist

from app.infrastructure.db.models.tokenModel import RefreshTokenModel
from app.infrastructure.db.mappers.refreshTokenMapper import RefreshTokenMapper

class SQLAlchemyRefreshTokenRepository(RefreshTokenRepository):

    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def add(self, token: RefreshToken)-> None:
              model = RefreshTokenMapper.to_orm(token)
              self.session.add(model)

    async def get_by_hash(self, token_hash: str) -> RefreshToken | None:
          try:
            stmt = select(RefreshTokenModel).where(RefreshTokenModel.token_hash == token_hash)
            result = await self.session.execute(stmt)
            orm_token = result.scalars().first()

            if not orm_token:
                    return None
            return RefreshTokenMapper.to_domain(orm_token)
          except IntegrityError:
                raise RegisterNotExist()
                
    
    async def revoke(self, token_id: UUID):
        try:
                stmt = select(RefreshTokenModel).where(RefreshTokenModel.id == token_id)
                result = await self.session.execute(stmt)
                orm_token = result.scalars().first()

                if orm_token:
                      orm_token.revoked = True
        except IntegrityError:
              raise RegisterNotExist()

        