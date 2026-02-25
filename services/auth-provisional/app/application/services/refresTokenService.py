from app.domain.unit_of_work import AbstractUnitOfWork
from app.domain.entities.refresh_token import RefreshToken
from app.domain.services.token_service import TokenService
from app.domain.services.password_hasher import PasswordHasher

class RefreshTokenService:

    def __init__(self) -> None:
        pass

    # async def refresh(self, refresh_token: str):

    #     token_hash = self.hasher.hash(refresh_token)

    #     async with self.uow as uow:

    #         stored = await uow.refresh_tokens.get_by_hash(token_hash)

    #         if not stored:
    #             raise InvalidCredentials()

    #         if stored.revoked or stored.is_expired():
    #             raise InvalidCredentials()

    #         stored.revoke()

    #         new_access = self.token_service.generate_access(stored.user_id)
    #         new_refresh = self.token_service.generate_refresh(stored.user_id)

    #         # guardar nuevo refresh
    #         new_hash = self.hasher.hash(new_refresh)

    #         new_entity = RefreshToken(
    #             id=uuid4(),
    #             user_id=stored.user_id,
    #             token_hash=new_hash,
    #             expires_at=datetime.utcnow() + timedelta(days=7)
    #         )

    #         await uow.refresh_tokens.add(new_entity)

    #         await uow.commit()

    #         return {
    #             "access_token": new_access,
    #             "refresh_token": new_refresh
    #         }