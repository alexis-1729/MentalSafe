from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import user_auth as UserAuth
from app.schemas.auth import LoginForm, Token, UserAuthUpdate, UserAuthRegister
from app.services.token import *

def login_user(form: LoginForm, db: Session):
    user = db.query(UserAuth).filter(UserAuth.username == form.username).first()
    if not user or not verify_password(form.password, user.password_h):
        raise HTTPException(status_code = 404, detail = "User not found")
    token = create_acess_token({
        "sub": user.username,
        "role": user.role})
    return {"id":user.id,"acces_token": token, "token_type": "bearer"}

def register_user(form: LoginForm, db: Session):
    user = db.query(UserAuth).filter(UserAuth.username == form.username).first()
    if user:
        raise HTTPException(status_code = 404, detail = "user alredy exist")
    hashed = get_password_hash(form.password)
    user = UserAuth(username = form.username, password_h = hashed)

    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User created", "username": user.username}

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
    