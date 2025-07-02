from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database,  auth
from app.schemas.auth import LoginForm, Token


router = APIRouter(prefix = "/auth", tags = ["auth"])

@router.post("/login", response_model = Token)
def login(form: LoginForm, db:Session = Depends(database.get_db)):
    user = db.query(models.user_auth).filter(models.user_auth.username== form.username).first()
    if not user or not auth.verify_password(form.password, user.password_h):
        raise HTTPException(status_code = 400, detail = "Invalid credentials")
    access_token = auth.create_acess_token(data = {"sub":user.username})
    return {"access_token": access_token, "token_type":"bearer"}

@router.post("/register")
def register(form: LoginForm, db: Session = Depends(database.get_db)):
    existing = db.query(models.user_auth).filter(models.user_auth.username == form.username).first()
    if existing:
        raise HTTPException(status_code = 400, detail = "user alredy registred")
    hashed = auth.get_password_hash(form.password)
    user = models.user_auth( username = form.username, password_h = hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User created", "username": user.username}
