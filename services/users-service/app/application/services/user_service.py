from uuid import UUID, uuid4
from app.domain.entities.user import User
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.domain.exceptions import UserNotFound
from app.api.schemas.userSchemas import UserCreate
from datetime import datetime

class UserService:
    def __init__(self, uow: UnitOfWorkImpl):
        self.uow = uow

    async def create_user(self, user_data: UserCreate) -> User:
        """Crear un nuevo usuario siguiendo el esquema simplificado (Punto 5)"""
        with self.uow as uow:
            existing = await uow.users.get_by_id_auth(user_data.id_auth)
            if existing:
                raise ValueError("El usuario ya existe con ese id_auth")
            
            new_user = User(
                id=uuid4(), 
                id_auth=user_data.id_auth,
                full_name=user_data.full_name,
                apellidos=user_data.apellidos,
                fecha_nac=user_data.fecha_nac,
                genero=user_data.genero,
                created_at=datetime.utcnow()
            )
            
            await uow.users.add(new_user)
            return new_user

    async def get_user_by_id(self, user_id: UUID) -> User:
        """Obtener un usuario por ID (UUID)"""
        with self.uow as uow:
            user = await uow.users.get_by_id(user_id)
            if not user:
                raise UserNotFound(f"Usuario con id {user_id} no encontrado")
            return user

    async def get_all_users(self) -> list[User]:
        """Obtener todos los usuarios"""
        with self.uow as uow:
            return await uow.users.get_all()