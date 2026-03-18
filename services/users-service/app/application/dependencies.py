from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.db.database import get_db
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services.userService import UserService

def get_user_service(db: Session = Depends(get_db)):
    uow = UnitOfWorkImpl(db)
    return UserService(uow)