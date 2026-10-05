from app.infrastructure.db.models.resultTestModel import ResultTestModel
from app.domain.entities.result_test import ResultTestEntity


class ResultTestMapper:
    """Mapper para convertir ResultTestModel a ResultTestEntity y viceversa"""

    @staticmethod
    def to_entity(model: ResultTestModel) -> ResultTestEntity | None:
        """Convierte un modelo SQLAlchemy a una entidad de dominio"""
        if not model:
            return None
        
        return ResultTestEntity(
            result_id=model.result_id,
            score=model.score,
            id_test=model.id_test,
            test=None,  # Se cargan con relaciones si es necesario
            test_users=None,  # Se cargan con relaciones si es necesario
        )

    @staticmethod
    def to_model(entity: ResultTestEntity) -> ResultTestModel:
        """Convierte una entidad de dominio a un modelo SQLAlchemy"""
        if not entity:
            return None
        
        model = ResultTestModel(
            result_id=entity.result_id,
            score=entity.score,
            id_test=entity.id_test,
        )
        return model

    @staticmethod
    def to_entities(models: list) -> list:
        """Convierte una lista de modelos SQLAlchemy a entidades"""
        return [ResultTestMapper.to_entity(model) for model in models]
