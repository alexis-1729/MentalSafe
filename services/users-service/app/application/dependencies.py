from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services.userService import UserService

async def get_user_service(db: AsyncSession = Depends(get_db)):
    uow = UnitOfWorkImpl(db)
    return UserService(uow)