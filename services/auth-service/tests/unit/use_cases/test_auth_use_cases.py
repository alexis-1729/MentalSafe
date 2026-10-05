from app.domain.entities.auth import Auth
import uuid 

class RegisterUserUseCase:
    def __init__(self, uow, hasher):
        self.uow = uow
        self.hasher = hasher

    async def execute(self, email, password):
        async with self.uow:
            existing = await self.uow.auth.get(email)
            if existing:
                raise Exception("user alredy exists")
            
            hashed = self.hasher.hash(password)

            user = Auth(uuid.uuid4(), email=email, password_h= hashed, role = "admin")

            await self.uow.users.add(user)
            await self.uow.commit()
            return user.id
        
class LoginUserUseCase:
    def __init__(self, uow, hasher, jwt_service):
        self.uow = uow
        self.hasher = hasher
        self.jwt_service = jwt_service

    async def execute(self, email, password):
        async with self.uow:
            user = await self.uow.users.get_by_email(email)
            if not user:
                raise Exception("Invalid credentials")

            if not self.hasher.verify(password, user.password_h):
                raise Exception("Invalid credentials")

            token = self.jwt_service.generate(user.id)
            return token