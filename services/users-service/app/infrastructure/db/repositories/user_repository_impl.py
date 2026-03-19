from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from typing import Optional
from app.domain.repositories.userRepository import UserRepository
from app.infrastructure.db.models.userModel import UserModel
from app.infrastructure.db.mappers.userMapper import UserMapper
from app.domain.entities.user import User

class UserRepositoryImpl(UserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add(self, user: User) -> None:
        """Agregar un nuevo usuario"""
        model = UserMapper.to_model(user)
        self.db.add(model)
        await self.db.flush()

    async def get_by_id(self, id: UUID) -> Optional[User]:
        """Obtener un usuario por ID"""
        stmt = select(UserModel).where(UserModel.id == id)
        result = await self.db.execute(stmt)
        model = result.scalar_one_or_none()
        return UserMapper.to_entity(model)

    async def get_by_id_auth(self, id_auth: UUID) -> Optional[User]:
        """Obtener un usuario por ID de autenticación"""
        stmt = select(UserModel).where(UserModel.id_auth == id_auth)
        result = await self.db.execute(stmt)
        model = result.scalar_one_or_none()
        return UserMapper.to_entity(model)

    async def get_all(self) -> list[User]:
        """Obtener todos los usuarios"""
        stmt = select(UserModel)
        result = await self.db.execute(stmt)
        models = result.scalars().all()
        users = [UserMapper.to_entity(m) for m in models]
        return [u for u in users if u is not None]