from app.domain.entities.user import User
from app.infrastructure.db.models.userModel import UserModel

class UserMapper:
    @staticmethod
    def to_entity(model: UserModel) -> User | None:
        if not model: return None
        return User(
            id=model.id,
            id_auth= model.id_auth,
            full_name=model.full_name,
            apellidos= model.apellidos,
            fecha_nac= model.fecha_nac,
            genero = model.genero,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            id_auth = entity.id_auth,
            full_name=entity.full_name,
            apellidos = entity.apellidos,
            fecha_nac = entity.fecha_nac,
            genero = entity.genero,
            created_at = entity.created_at,
            updated_at = entity.updated_at

        )