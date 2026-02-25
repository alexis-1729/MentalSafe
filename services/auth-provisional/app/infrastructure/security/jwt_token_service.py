from jose import jwt
from datetime import datetime, timedelta
from app.domain.services.token_service import TokenService
from uuid import UUID
from dotenv import load_dotenv
import os

load_dotenv()

class JWTTokenService(TokenService):
    
    def generate_access(self, user_id: UUID) -> str:
        expire = datetime.utcnow() + timedelta(
            minutes= os.getenv('ACCESS_TOKEN_EXPIRE_MIN')
        )
        payload = {
            "sub": str(user_id),
            "type": "access",
            "exp": expire
        }

        return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))

    def generate_refresh(self, user_id: UUID) -> str:
        payload = {
            "sub": str(user_id),
            "type": "refresh",
            "exp": datetime.utcnow() + timedelta(days=os.getenv('REFRESH_EXPIRE_DAYS'))
        }
        return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))

    def verify(self, token: str) -> UUID:
        try:
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
            return UUID(payload["sub"])
        except JWTError:
            raise Exception("Invalid token")