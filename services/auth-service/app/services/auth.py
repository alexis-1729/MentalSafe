from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import user_auth as UserAuth
from app.schemas.auth import LoginForm, Token, UserAuthUpdate, UserAuthRegister
from app.services.token import *

def login_user(form: LoginForm, db: Session):
    user = db.query(UserAuth).filter(UserAuth.username == form.username).first()
    if not user or not verify_password(form.password, user.password_h):
        raise HTTPException(status_code = 404, detail = "User not found")
    
    access_token = create_acess_token({
        "sub": user.id,
        "role": user.role})
    refresh_token = create_refresh_token({
        "sub": user.id,
        "role": user.role}, db)
    
    return {"acces_token": access_token,"refresh_token": refresh_token, "token_type": "bearer"}

# ·agregar el acces_token y refresh y enviar el user_id
def register_user(form: LoginForm, db: Session):
    user = db.query(UserAuth).filter(UserAuth.username == form.username).first()
    if user:
        raise HTTPException(status_code = 404, detail = "user alredy exist")
    hashed = get_password_hash(form.password)
    user = UserAuth(username = form.username, password_h = hashed, role = form.role)

    db.add(user)
    db.commit()
    db.refresh(user)

    access_token = create_acess_token({
        "sub": user.id,
        "role": form.role})
    
    refresh_token = create_refresh_token({
        "sub": user.id,
        "role": form.role}, db)

    return {"acces_token": access_token,"refresh_token": refresh_token, "token_type": "bearer"}

def logout(refresh_token: str, db: Session):
    try:
        payload = jwt.decode(refresh_token, os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM"))
        jti = payload.get("jti")
        token = db.query(token_auth).filter(token_auth.jti == jti).first()
        
        if not token:
            raise HTTPException(status_code = 401, detail = "Not found token")

        db.delete(token)
        db.commit()
    except JWTError:
        raise HTTPException(status_code = 401, detail = "Token invalido")

def get_user(db: Session, username: str)-> UserAuth | None:
    user = db.query(UserAuth).filter(UserAuth.username == username).first()
    if not user:
        return None
    return user

def update_user(db: Session, new: UserAuthUpdate, username: str):
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code = 404, detail = "user not found")
    
    user.username = new.username
    user.password_h = get_password_hash(new.password)
    db.commit()
    db.refresh(user)
    return {"msg": "user updated", "username": user.username}

def delete_user(db: Session, username: str):
    user = get_user(db, username)
    if not user :
        raise HTTPException(status_code = 404, detail = "User not found")
    db.delete(user)
    db.commit()
    return {"msg": "User '{username}' deleted"}
    