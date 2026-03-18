from app.domain.entities.user import User
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.api.schemas.userSchemas import UserCreate
from fastapi import HTTPException, status

class UserService:
    def __init__(self, uow: UnitOfWorkImpl):
        self.uow = uow

    def register_user(self, user_data: UserCreate) -> User:
        with self.uow:
            existing = self.uow.users.find_by_email(user_data.email)
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El usuario ya existe con ese correo."
                )
            
            new_user = User(
                id=None,
                username=user_data.username,
                email=user_data.email,
                password=user_data.password, 
                full_name=user_data.full_name
            )
            
            return self.uow.users.save(new_user)