from app.domain.entities.auth import Auth
from app.infrastructure.db.models.authModel import AuthORM

class AuthMapper:

    @staticmethod
    def to_domain(orm: AuthORM)-> Auth:
        
        return Auth(
            id= orm.id,
            email= orm.email,
            password_h= orm.password_h,
            role = orm.role
        )
    
    @staticmethod
    def to_orm(entity: Auth) -> AuthORM:
        return AuthORM(
            id = entity.id,
            email = entity.email,
            password_h = entity.password_h,
            role = entity.role
        )