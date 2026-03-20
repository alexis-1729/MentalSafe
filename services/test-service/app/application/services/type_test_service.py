from typing import Optional, List
from uuid import UUID
from app.domain.unit_of_work import IUnitOfWork
from app.domain.entities.type_test import TypeTestEntity


class TypeTestService:
    """Servicio de TypeTest"""

    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    async def create_type_test(self, name_test: str, num_q: int) -> TypeTestEntity:
        """Crea un nuevo tipo de test"""
        entity = TypeTestEntity(
            typeT_id=None,  # Se genera automáticamente
            name_test=name_test,
            num_q=num_q,
        )
        created = await self.unit_of_work.type_test.create(entity)
        await self.unit_of_work.commit()
        return created

    async def get_type_test_by_id(self, typeT_id: UUID) -> Optional[TypeTestEntity]:
        """Obtiene un tipo de test por su ID"""
        return await self.unit_of_work.type_test.get_by_id(typeT_id)

    async def get_all_type_tests(self) -> List[TypeTestEntity]:
        """Obtiene todos los tipos de test"""
        return await self.unit_of_work.type_test.get_all()

    async def update_type_test(self, typeT_id: UUID, name_test: str, num_q: int) -> TypeTestEntity:
        """Actualiza un tipo de test"""
        entity = TypeTestEntity(
            typeT_id=typeT_id,
            name_test=name_test,
            num_q=num_q,
        )
        updated = await self.unit_of_work.type_test.update(entity)
        await self.unit_of_work.commit()
        return updated

    async def delete_type_test(self, typeT_id: UUID) -> bool:
        """Elimina un tipo de test"""
        result = await self.unit_of_work.type_test.delete(typeT_id)
        await self.unit_of_work.commit()
        return result
