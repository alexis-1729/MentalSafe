from fastapi import Depends
from sqlalchemy.orm import Session
# Importamos get_db desde su nueva ubicación
from app.infrastructure.db.database import get_db
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services.test_user_service import TestUserService
from app.application.services.type_test_service import TypeTestService

# Inyectamos el Unit of Work
def get_unit_of_work(db: Session = Depends(get_db)):
    return UnitOfWorkImpl(db)

# Inyectamos el Servicio de Usuarios-Test
def get_test_user_service(uow: UnitOfWorkImpl = Depends(get_unit_of_work)):
    return TestUserService(uow)

# Inyectamos el Servicio de Tipos de Test (por si necesitas crear nuevos tests)
def get_type_test_service(uow: UnitOfWorkImpl = Depends(get_unit_of_work)):
    return TypeTestService(uow)