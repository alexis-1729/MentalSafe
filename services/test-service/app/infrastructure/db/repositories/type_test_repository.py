from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.repositories.type_test_repository import ITypeTestRepository
from app.domain.entities.type_test import TypeTestEntity
from app.infrastructure.db.models.typeTestModel import TypeTestModel
from app.infrastructure.db.mappers.type_test_mapper import TypeTestMapper


class TypeTestRepository(ITypeTestRepository):
    """Implementación del repositorio de TypeTest"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.mapper = TypeTestMapper()

    async def create(self, entity: TypeTestEntity) -> TypeTestEntity:
        """Crea un nuevo tipo de test"""
        model = self.mapper.to_model(entity)
        self.session.add(model)
        await self.session.flush()
        return self.mapper.to_entity(model)

    async def get_by_id(self, typeT_id: UUID) -> Optional[TypeTestEntity]:
        """Obtiene un tipo de test por su ID"""
        statement = select(TypeTestModel).where(TypeTestModel.typeT_id == typeT_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        return self.mapper.to_entity(model) if model else None

    async def get_all(self) -> List[TypeTestEntity]:
        """Obtiene todos los tipos de test"""
        statement = select(TypeTestModel)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)

    async def update(self, entity: TypeTestEntity) -> TypeTestEntity:
        """Actualiza un tipo de test"""
        model = await self.get_by_id(entity.typeT_id)
        if not model:
            raise ValueError(f"TypeTest con ID {entity.typeT_id} no encontrado")
        
        statement = select(TypeTestModel).where(TypeTestModel.typeT_id == entity.typeT_id)
        result = await self.session.execute(statement)
        db_model = result.scalars().first()
        
        db_model.name_test = entity.name_test
        db_model.num_q = entity.num_q
        
        await self.session.flush()
        return self.mapper.to_entity(db_model)

    async def delete(self, typeT_id: UUID) -> bool:
        """Elimina un tipo de test"""
        statement = select(TypeTestModel).where(TypeTestModel.typeT_id == typeT_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        
        if model:
            await self.session.delete(model)
            await self.session.flush()
            return True
        return False
