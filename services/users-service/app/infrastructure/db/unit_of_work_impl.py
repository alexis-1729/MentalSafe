from sqlalchemy.orm import Session
from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl

class UnitOfWorkImpl:
    def __init__(self, session: Session = None):
        # Si no se pasa una sesión, se crea una nueva desde SessionLocal
        self.session = session if session else SessionLocal()
        # Aquí se inyectan todos los repositorios del microservicio
        self.users = UserRepositoryImpl(self.session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.session.commit()
            else:
                self.session.rollback()
        finally:
            self.session.close()