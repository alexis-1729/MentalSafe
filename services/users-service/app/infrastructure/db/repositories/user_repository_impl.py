from sqlalchemy.orm import Session
from app.domain.repositories.userRepository import UserRepository
from app.infrastructure.db.models.userModel import UserModel
from app.infrastructure.db.mappers.userMapper import UserMapper

class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, user):
        model = UserMapper.to_model(user)
        self.db.add(model)
        self.db.flush()
        return UserMapper.to_entity(model)

    def find_by_email(self, email: str):
        model = self.db.query(UserModel).filter(UserModel.email == email).first()
        return UserMapper.to_entity(model)