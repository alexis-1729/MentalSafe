from fastapi import Depends
from app.application.services.authService import AuthService
from app.infrastructure.db.dependencies import get_uow
from app.infrastructure.security.bcrypt_hasher import BcryptPasswordHasher
from app.infrastructure.security.jwt_token_service import JWTTokenService
from app.domain.unit_of_work import AbstractUnitOfWork

def get_auth_service(
        uow: AbstractUnitOfWork = Depends(get_uow)
):
    return AuthService(
                uow,
                hasher= BcryptPasswordHasher(),
                token_service= JWTTokenService()
                )
def get_refresh_token_service(
        uow: AbstractUnitOfWork = Depends(get_)
)