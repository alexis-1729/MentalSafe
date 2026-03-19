from app.domain.unit_of_work import AbstractUnitOfWork
from app.domain.entities.auth import Auth
from app.domain.services.password_hasher import PasswordHasher
from app.domain.services.token_service import TokenService
from app.domain.exceptions import InvalidPassword
from uuid import uuid4, UUID

class AuthService:

    def __init__(
            self, 
            uow: AbstractUnitOfWork,
            hasher: PasswordHasher,
            token_service: TokenService
            ):
                self.uow = uow
                self.hasher = hasher
                self.token_service = token_service

    async def register(self, email: str, password_h: str, role: str):

        async with self.uow as uow:
            
            hashed = self.hasher.hash(password_h)

            auth = Auth(
                id= uuid4(),
                email=email,
                password_h=hashed,
                role=role
            )

            await uow.auth.add(auth)
            await uow.commit()

            return auth
        
    async def login(self, email: str, password: str):
        async with self.uow as uow:

            user = await uow.auth.get(email)

            if not user:
                 raise InvalidPassword()
            
            if not self.hasher.verify(password, user.password_h):
                 raise InvalidPassword()
            
            access = self.token_service.generate_access(user.id)
            refresh = self.token_service.generate_refresh(user.id)

            
            return {
                 "access_token": user.id,
                 "refresh_token": refresh
            }