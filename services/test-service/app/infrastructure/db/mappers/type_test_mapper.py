from app.infrastructure.db.models.typeTestModel import TypeTestModel
from app.domain.entities.type_test import TypeTestEntity


class TypeTestMapper:
    """Mapper para convertir TypeTestModel a TypeTestEntity y viceversa"""

    @staticmethod
    def to_entity(model: TypeTestModel) -> TypeTestEntity:
        """Convierte un modelo SQLAlchemy a una entidad de dominio"""
        if not model:
            return None
        
        return TypeTestEntity(
            typeT_id=model.typeT_id,
            name_test=model.name_test,
            num_q=model.num_q,
            results=None,  # Se cargan con relaciones si es necesario
            tags=None,  # Se cargan con relaciones si es necesario
        )

    @staticmethod
    def to_model(entity: TypeTestEntity) -> TypeTestModel:
        """Convierte una entidad de dominio a un modelo SQLAlchemy"""
        if not entity:
            return None
        
        model = TypeTestModel(
            typeT_id=entity.typeT_id,
            name_test=entity.name_test,
            num_q=entity.num_q,
        )
        return model

    @staticmethod
    def to_entities(models: list) -> list:
        """Convierte una lista de modelos SQLAlchemy a entidades"""
        return [TypeTestMapper.to_entity(model) for model in models]
