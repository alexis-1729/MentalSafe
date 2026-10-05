from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.repositories.test_user_repository import ITestUserRepository
from app.domain.entities.test_user import TestUserEntity
from app.infrastructure.db.models.testUserModel import TestUserModel
from app.infrastructure.db.mappers.test_user_mapper import TestUserMapper


class TestUserRepository(ITestUserRepository):
    """Implementación del repositorio de TestUser"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.mapper = TestUserMapper()

    async def create(self, entity: TestUserEntity) -> TestUserEntity:
        """Crea una nueva relación usuario-test"""
        model = self.mapper.to_model(entity)
        self.session.add(model)
        await self.session.flush()
        return self.mapper.to_entity(model)

    async def get_by_id(self, test_id: UUID) -> Optional[TestUserEntity]:
        """Obtiene una relación usuario-test por su ID"""
        statement = select(TestUserModel).where(TestUserModel.test_id == test_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        return self.mapper.to_entity(model) if model else None

    async def get_all(self) -> List[TestUserEntity]:
        """Obtiene todas las relaciones usuario-test"""
        statement = select(TestUserModel)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)

    async def update(self, entity: TestUserEntity) -> TestUserEntity:
        """Actualiza una relación usuario-test"""
        model = await self.get_by_id(entity.test_id)
        if not model:
            raise ValueError(f"TestUser con ID {entity.test_id} no encontrado")
        
        statement = select(TestUserModel).where(TestUserModel.test_id == entity.test_id)
        result = await self.session.execute(statement)
        db_model = result.scalars().first()
        
        db_model.id_user = entity.id_user
        db_model.result_id = entity.result_id
        db_model.created_at = entity.created_at
        
        await self.session.flush()
        return self.mapper.to_entity(db_model)

    async def delete(self, test_id: UUID) -> bool:
        """Elimina una relación usuario-test"""
        statement = select(TestUserModel).where(TestUserModel.test_id == test_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        
        if model:
            await self.session.delete(model)
            await self.session.flush()
            return True
        return False

    async def get_by_user_id(self, id_user: UUID) -> List[TestUserEntity]:
        """Obtiene todos los tests de un usuario específico"""
        statement = select(TestUserModel).where(TestUserModel.id_user == id_user)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)

    async def get_by_result_id(self, result_id: UUID) -> List[TestUserEntity]:
        """Obtiene todas las relaciones usuario-test de un resultado específico"""
        statement = select(TestUserModel).where(TestUserModel.result_id == result_id)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)
