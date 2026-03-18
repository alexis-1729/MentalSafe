from sqlalchemy.orm import Session
from app.infrastructure.db.repositories.chat_repository_impl import ChatRepositoryImpl

class UnitOfWorkImpl:
    def __init__(self, session: Session):
        self.session = session
        self.chats = ChatRepositoryImpl(session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()