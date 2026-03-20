from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.repositories.result_test_repository import IResultTestRepository
from app.domain.entities.result_test import ResultTestEntity
from app.infrastructure.db.models.resultTestModel import ResultTestModel
from app.infrastructure.db.mappers.result_test_mapper import ResultTestMapper


class ResultTestRepository(IResultTestRepository):
    """Implementación del repositorio de ResultTest"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.mapper = ResultTestMapper()

    async def create(self, entity: ResultTestEntity) -> ResultTestEntity:
        """Crea un nuevo resultado de test"""
        model = self.mapper.to_model(entity)
        self.session.add(model)
        await self.session.flush()
        return self.mapper.to_entity(model)

    async def get_by_id(self, result_id: UUID) -> Optional[ResultTestEntity]:
        """Obtiene un resultado de test por su ID"""
        statement = select(ResultTestModel).where(ResultTestModel.result_id == result_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        return self.mapper.to_entity(model) if model else None

    async def get_all(self) -> List[ResultTestEntity]:
        """Obtiene todos los resultados de test"""
        statement = select(ResultTestModel)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)

    async def update(self, entity: ResultTestEntity) -> ResultTestEntity:
        """Actualiza un resultado de test"""
        model = await self.get_by_id(entity.result_id)
        if not model:
            raise ValueError(f"ResultTest con ID {entity.result_id} no encontrado")
        
        statement = select(ResultTestModel).where(ResultTestModel.result_id == entity.result_id)
        result = await self.session.execute(statement)
        db_model = result.scalars().first()
        
        db_model.score = entity.score
        db_model.id_test = entity.id_test
        
        await self.session.flush()
        return self.mapper.to_entity(db_model)

    async def delete(self, result_id: UUID) -> bool:
        """Elimina un resultado de test"""
        statement = select(ResultTestModel).where(ResultTestModel.result_id == result_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        
        if model:
            await self.session.delete(model)
            await self.session.flush()
            return True
        return False

    async def get_by_test_id(self, id_test: UUID) -> List[ResultTestEntity]:
        """Obtiene todos los resultados de un tipo de test específico"""
        statement = select(ResultTestModel).where(ResultTestModel.id_test == id_test)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)
