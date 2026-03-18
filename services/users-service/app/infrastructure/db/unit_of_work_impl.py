from sqlalchemy.orm import Session
from app.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl

class UnitOfWorkImpl:
    def __init__(self, session: Session):
        self.session = session
        self.users = UserRepositoryImpl(session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()