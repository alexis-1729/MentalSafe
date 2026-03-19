from app.infrastructure.db.models.tagTestModel import TagTestModel
from app.domain.entities.tag_test import TagTestEntity


class TagTestMapper:
    """Mapper para convertir TagTestModel a TagTestEntity y viceversa"""

    @staticmethod
    def to_entity(model: TagTestModel) -> TagTestEntity:
        """Convierte un modelo SQLAlchemy a una entidad de dominio"""
        if not model:
            return None
        
        return TagTestEntity(
            tag_id=model.tag_id,
            name=model.name,
            id_test_type=model.id_test_type,
            type=None,  # Se cargan con relaciones si es necesario
        )

    @staticmethod
    def to_model(entity: TagTestEntity) -> TagTestModel:
        """Convierte una entidad de dominio a un modelo SQLAlchemy"""
        if not entity:
            return None
        
        model = TagTestModel(
            tag_id=entity.tag_id,
            name=entity.name,
            id_test_type=entity.id_test_type,
        )
        return model

    @staticmethod
    def to_entities(models: list) -> list:
        """Convierte una lista de modelos SQLAlchemy a entidades"""
        return [TagTestMapper.to_entity(model) for model in models]
