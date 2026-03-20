from typing import Optional, List
from uuid import UUID
from datetime import datetime
from app.domain.unit_of_work import IUnitOfWork
from app.domain.entities.test_user import TestUserEntity


class TestUserService:
    """Servicio de TestUser"""

    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    async def create_test_user(self, id_user: UUID, result_id: UUID) -> TestUserEntity:
        """Crea una nueva relación usuario-test"""
        entity = TestUserEntity(
            test_id=None,  # Se genera automáticamente
            id_user=id_user,
            result_id=result_id,
            created_at=datetime.now(),
        )
        created = await self.unit_of_work.test_user.create(entity)
        await self.unit_of_work.commit()
        return created

    async def get_test_user_by_id(self, test_id: UUID) -> Optional[TestUserEntity]:
        """Obtiene una relación usuario-test por su ID"""
        return await self.unit_of_work.test_user.get_by_id(test_id)

    async def get_all_test_users(self) -> List[TestUserEntity]:
        """Obtiene todas las relaciones usuario-test"""
        return await self.unit_of_work.test_user.get_all()

    async def update_test_user(self, test_id: UUID, id_user: UUID, result_id: UUID) -> TestUserEntity:
        """Actualiza una relación usuario-test"""
        entity = TestUserEntity(
            test_id=test_id,
            id_user=id_user,
            result_id=result_id,
            created_at=datetime.now(),
        )
        updated = await self.unit_of_work.test_user.update(entity)
        await self.unit_of_work.commit()
        return updated

    async def delete_test_user(self, test_id: UUID) -> bool:
        """Elimina una relación usuario-test"""
        result = await self.unit_of_work.test_user.delete(test_id)
        await self.unit_of_work.commit()
        return result

    async def get_tests_by_user(self, id_user: UUID) -> List[TestUserEntity]:
        """Obtiene todos los tests de un usuario"""
        return await self.unit_of_work.test_user.get_by_user_id(id_user)

    async def get_test_users_by_result(self, result_id: UUID) -> List[TestUserEntity]:
        """Obtiene todas las relaciones usuario-test de un resultado"""
        return await self.unit_of_work.test_user.get_by_result_id(result_id)
