from app.infrastructure.db.unit_of_work import SQLAlchemyUnitOfWork
from app.infrastructure.db.database import get_db

def get_uow():
    return SQLAlchemyUnitOfWork(get_db)