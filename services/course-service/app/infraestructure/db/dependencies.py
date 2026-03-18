from app.infraestructure.db.unit_of_work import SQLAlchemyUnitOfWork
from app.infraestructure.database import get_db

def get_uow():
    return SQLAlchemyUnitOfWork(get_db)
