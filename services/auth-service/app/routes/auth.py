from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.services.auth import *
from app.services.token import *
from app.schemas.auth import LoginForm, UserAuthUpdate, Token, TokenData
from app.database import get_db

router = APIRouter(prefix = "/auth", tags = ["auth"])

@router.post("/login")
def login_route(form: LoginForm, db:Session = Depends(get_db)):
   return login_user(form, db)

@router.post("/register")
def register_route(form: LoginForm, db: Session = Depends(get_db)):
    return register_user(form, db)

@router.post("/logout")
def  logout_route(refresh_token: str, db: Session = Depends(get_db)):
    return logout(refresh_token, db)

@router.post("/refresh", response_model= Token)
def refresh_token_route(refresh_t: str, db: Session=Depends(get_db)):
    return refresh_token(refresh_t, db)


#------ Actualizar cuenta con verificacion JWT-----#
@router.put("/users/{username}")
def update_user_route(
    new: UserAuthUpdate,
    username: str = Path(..., description="Current username"),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
    ):
    if username != current_user.username:
        raise HTTPException(status_code = 404, detail = "Unauthorized")
    return update_user(db, new, username)


@router.delete("/users/{username}")
def delete_user_route(db: Session = Depends(get_db), 
    username: str = Path(..., description =  "Username to delete"),
    current_user: str = Depends(get_current_user)
    ):
    if username != current_user.username:
        raise HTTPException(status_code = 404, detail = current_user)
        
    return delete_user(db, username)

