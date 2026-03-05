import bcrypt 
from app.domain.services.password_hasher import PasswordHasher

class BcryptPasswordHasher(PasswordHasher):
    def hash(self, password: str) -> str:
        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()
    
    def verify(self, plain: str, hashed: str) -> bool:
        return bcrypt.checkpw(
            plain.encode(),
            hashed.encode()
        )