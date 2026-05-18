from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.db.database import get_db
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services.user_service import UserService

def get_unit_of_work(db: Session = Depends(get_db)):
    return UnitOfWorkImpl(db)

def get_user_service(uow: UnitOfWorkImpl = Depends(get_unit_of_work)):
    return UserService(uow)