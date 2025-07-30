from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from dotenv import load_dotenv
from app.schemas.auth import TokenData, CurrentUser
import os
load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_acess_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes = int(os.getenv("AC_TOKEN_MINUTE"))))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm = os.getenv("ALGORITHM"))
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme))-> CurrentUser:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms = os.getenv("ALGORITHM"))
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if not username or not role:
            raise credentials_exception
        return CurrentUser(username = username, role = role)
    except JWTError:
        raise credentials_exception