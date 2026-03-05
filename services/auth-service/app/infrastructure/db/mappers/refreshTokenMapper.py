from app.domain.entities.refresh_token import RefreshToken
from app.infrastructure.db.models.tokenModel import RefreshTokenModel

class RefreshTokenMapper:

    @staticmethod
    def to_domain(model: RefreshTokenModel)-> RefreshToken:
        return RefreshToken(
            id= model.id,
            auth_id = model.auth_id,
            token_hash = model.token_hash,
            expires_at = model.expires_at,
            revoked = model.revoked
        )
    
    @staticmethod
    def to_orm(entity: RefreshToken) -> RefreshTokenModel:
        return RefreshTokenModel(
            id = entity.id,
            auth_id = entity.auth_id,
            token_hash = entity.token_hash,
            expires_at = entity.expires_at,
            revoked = entity.revoked
        )