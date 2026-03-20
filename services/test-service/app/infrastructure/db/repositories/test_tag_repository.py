from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.repositories.tag_test_repository import ITagTestRepository
from app.domain.entities.tag_test import TagTestEntity
from app.infrastructure.db.models.tagTestModel import TagTestModel
from app.infrastructure.db.mappers.tag_test_mapper import TagTestMapper


class TagTestRepository(ITagTestRepository):
    """Implementación del repositorio de TagTest"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.mapper = TagTestMapper()

    async def create(self, entity: TagTestEntity) -> TagTestEntity:
        """Crea una nueva etiqueta de test"""
        model = self.mapper.to_model(entity)
        self.session.add(model)
        await self.session.flush()
        return self.mapper.to_entity(model)

    async def get_by_id(self, tag_id: UUID) -> Optional[TagTestEntity]:
        """Obtiene una etiqueta de test por su ID"""
        statement = select(TagTestModel).where(TagTestModel.tag_id == tag_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        return self.mapper.to_entity(model) if model else None

    async def get_all(self) -> List[TagTestEntity]:
        """Obtiene todas las etiquetas de test"""
        statement = select(TagTestModel)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)

    async def update(self, entity: TagTestEntity) -> TagTestEntity:
        """Actualiza una etiqueta de test"""
        model = await self.get_by_id(entity.tag_id)
        if not model:
            raise ValueError(f"TagTest con ID {entity.tag_id} no encontrado")
        
        statement = select(TagTestModel).where(TagTestModel.tag_id == entity.tag_id)
        result = await self.session.execute(statement)
        db_model = result.scalars().first()
        
        db_model.name = entity.name
        db_model.id_test_type = entity.id_test_type
        
        await self.session.flush()
        return self.mapper.to_entity(db_model)

    async def delete(self, tag_id: UUID) -> bool:
        """Elimina una etiqueta de test"""
        statement = select(TagTestModel).where(TagTestModel.tag_id == tag_id)
        result = await self.session.execute(statement)
        model = result.scalars().first()
        
        if model:
            await self.session.delete(model)
            await self.session.flush()
            return True
        return False

    async def get_by_test_type_id(self, id_test_type: UUID) -> List[TagTestEntity]:
        """Obtiene todas las etiquetas de un tipo de test específico"""
        statement = select(TagTestModel).where(TagTestModel.id_test_type == id_test_type)
        result = await self.session.execute(statement)
        models = result.scalars().all()
        return self.mapper.to_entities(models)
