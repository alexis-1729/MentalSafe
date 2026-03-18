from app.domain.entities.user import User
from app.infrastructure.db.models.userModel import UserModel

class UserMapper:
    @staticmethod
    def to_entity(model: UserModel) -> User:
        if not model: return None
        return User(
            id=model.id,
            username=model.username,
            email=model.email,
            password=model.password,
            full_name=model.full_name,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            username=entity.username,
            email=entity.email,
            password=entity.password,
            full_name=entity.full_name
        )