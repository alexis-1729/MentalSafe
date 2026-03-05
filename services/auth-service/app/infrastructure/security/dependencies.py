
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.infrastructure.security.jwt_token_service import JWTTokenService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

token_service = JWTTokenService()


async def get_current_user_id(token: str = Depends(oauth2_scheme)):

    try:
        return token_service.verify(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")