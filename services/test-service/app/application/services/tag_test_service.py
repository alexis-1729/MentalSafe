from typing import Optional, List
from uuid import UUID
from app.domain.unit_of_work import IUnitOfWork
from app.domain.entities.tag_test import TagTestEntity


class TagTestService:
    """Servicio de TagTest"""

    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    async def create_tag_test(self, name: str, id_test_type: UUID) -> TagTestEntity:
        """Crea una nueva etiqueta de test"""
        entity = TagTestEntity(
            tag_id=None,  # Se genera automáticamente
            name=name,
            id_test_type=id_test_type,
        )
        created = await self.unit_of_work.tag_test.create(entity)
        await self.unit_of_work.commit()
        return created

    async def get_tag_test_by_id(self, tag_id: UUID) -> Optional[TagTestEntity]:
        """Obtiene una etiqueta de test por su ID"""
        return await self.unit_of_work.tag_test.get_by_id(tag_id)

    async def get_all_tag_tests(self) -> List[TagTestEntity]:
        """Obtiene todas las etiquetas de test"""
        return await self.unit_of_work.tag_test.get_all()

    async def update_tag_test(self, tag_id: UUID, name: str, id_test_type: UUID) -> TagTestEntity:
        """Actualiza una etiqueta de test"""
        entity = TagTestEntity(
            tag_id=tag_id,
            name=name,
            id_test_type=id_test_type,
        )
        updated = await self.unit_of_work.tag_test.update(entity)
        await self.unit_of_work.commit()
        return updated

    async def delete_tag_test(self, tag_id: UUID) -> bool:
        """Elimina una etiqueta de test"""
        result = await self.unit_of_work.tag_test.delete(tag_id)
        await self.unit_of_work.commit()
        return result

    async def get_tags_by_test_type(self, id_test_type: UUID) -> List[TagTestEntity]:
        """Obtiene todas las etiquetas de un tipo de test"""
        return await self.unit_of_work.tag_test.get_by_test_type_id(id_test_type)
