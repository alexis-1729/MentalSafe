from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from dotenv import load_dotenv
import uuid
from app.schemas.auth import TokenData, CurrentUser
import os
from slqalchemy.orm import Session
from app.models import token_auth
load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)
#este 20 min
def create_acess_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes = int(os.getenv("AC_TOKEN_MINUTE"))))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm = os.getenv("ALGORITHM"))
    return encoded_jwt

#el refresh dura 7 dias
def create_refresh_token(data:dict, db: Session):
    expire = datetime.utcnow() + timedelta(days= int(os.getenv("RF_TOKEN_MINUTE")))
    jti = str(uuid.uuid4())
    token_data = data.copy()
    token_data.update({"jti":jti, "exp": expire})
    token = jwt.encode(token_data, os.getenv("SECRET_KEY"), algorithm= os.getenv("ALGORITHM"))
    
    #guardamos en db
    save_token = token_auth(jti = jti,sub = data["sub"], exp = data["exp"])
    db.add(save_token)
    db.commit()
    db.refresh(save_token)

    return token


#valido refresh y creo otro para cuando expire un acces token
def refresh_token(refresh_token: str, db: Session):
    try:
        payload = jwt.decode(refresh_token, os.getenv("SECRET_KEY"), algorithms= os.getenv("ALGORITHM"))
        jti = payload.get("jti")
        userid = payload.get("sub")

        #comprobar el la db
        save_token = db.query(token_auth).filter(
            and_(
                token_auth.jti == jti,
                token_auth.sub == userid
            )
        ).first()

        if not save_token:
            raise HTTPException(status_code = 401, detail = "refresh invalido")

        #valido
        access_token = create_acess_token()
        new_refresh_token = create_refresh_token()
        #invalidamos en la db el refresh anterior
        db.delete(save_token)
        db.commit()

        return {"acces_token": access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}
    
    except JWTError:
        raise HTTPException(status_code = 401, detail= "Token invalido")

def get_current_user(token: str = Depends(oauth2_scheme))-> CurrentUser:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms = os.getenv("ALGORITHM"))
        userid: str = payload.get("sub")
        role: str = payload.get("role")
        if not userid or not role:
            raise credentials_exception
        return CurrentUser(userid = userid, role = role)
    except JWTError:
        raise credentials_exception