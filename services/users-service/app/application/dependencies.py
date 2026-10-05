from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services.user_service import UserService

def get_unit_of_work(db: AsyncSession = Depends(get_db)):
    return UnitOfWorkImpl()

def get_user_service(uow: UnitOfWorkImpl = Depends(get_unit_of_work)):
    return UserService(uow)