from typing import Optional, List
from uuid import UUID
from app.domain.unit_of_work import IUnitOfWork
from app.domain.entities.result_test import ResultTestEntity


class ResultTestService:
    """Servicio de ResultTest"""

    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    async def create_result_test(self, score: int, id_test: UUID) -> ResultTestEntity:
        """Crea un nuevo resultado de test"""
        entity = ResultTestEntity(
            result_id=None,  # Se genera automáticamente
            score=score,
            id_test=id_test,
        )
        created = await self.unit_of_work.result_test.create(entity)
        await self.unit_of_work.commit()
        return created

    async def get_result_test_by_id(self, result_id: UUID) -> Optional[ResultTestEntity]:
        """Obtiene un resultado de test por su ID"""
        return await self.unit_of_work.result_test.get_by_id(result_id)

    async def get_all_result_tests(self) -> List[ResultTestEntity]:
        """Obtiene todos los resultados de test"""
        return await self.unit_of_work.result_test.get_all()

    async def update_result_test(self, result_id: UUID, score: int, id_test: UUID) -> ResultTestEntity:
        """Actualiza un resultado de test"""
        entity = ResultTestEntity(
            result_id=result_id,
            score=score,
            id_test=id_test,
        )
        updated = await self.unit_of_work.result_test.update(entity)
        await self.unit_of_work.commit()
        return updated

    async def delete_result_test(self, result_id: UUID) -> bool:
        """Elimina un resultado de test"""
        result = await self.unit_of_work.result_test.delete(result_id)
        await self.unit_of_work.commit()
        return result

    async def get_results_by_test_type(self, id_test: UUID) -> List[ResultTestEntity]:
        """Obtiene todos los resultados de un tipo de test"""
        return await self.unit_of_work.result_test.get_by_test_id(id_test)
