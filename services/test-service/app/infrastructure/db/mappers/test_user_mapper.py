from app.infrastructure.db.models.testUserModel import TestUserModel
from app.domain.entities.test_user import TestUserEntity


class TestUserMapper:
    """Mapper para convertir TestUserModel a TestUserEntity y viceversa"""

    @staticmethod
    def to_entity(model: TestUserModel) -> TestUserEntity:
        """Convierte un modelo SQLAlchemy a una entidad de dominio"""
        if not model:
            return None
        
        return TestUserEntity(
            test_id=model.test_id,
            id_user=model.id_user,
            result_id=model.result_id,
            created_at=model.created_at,
            result=None,  # Se cargan con relaciones si es necesario
        )

    @staticmethod
    def to_model(entity: TestUserEntity) -> TestUserModel:
        """Convierte una entidad de dominio a un modelo SQLAlchemy"""
        if not entity:
            return None
        
        model = TestUserModel(
            test_id=entity.test_id,
            id_user=entity.id_user,
            result_id=entity.result_id,
            created_at=entity.created_at,
        )
        return model

    @staticmethod
    def to_entities(models: list) -> list:
        """Convierte una lista de modelos SQLAlchemy a entidades"""
        return [TestUserMapper.to_entity(model) for model in models]
