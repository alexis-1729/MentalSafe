from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import *
from sqlalchemy.orm import Session
from app.services.ia_sessions import *
from app.services.ia_messages import *
from app.database import get_db
import uuid

router = APIRouter(
    prefix = "/chating",
    tags = ["Chating"]
)


@router.post("/{user_id}")
def init_chat(user_id: str, data: ChatMessageCreate,db: Session = Depends(get_db)):
    new = ChatSessionCreate(
        user_id=user_id,
        title = "NEW"
    )
    #creamos sesion
    session = create_new_session(new, db)
    #creamos mensaje y recibimos respuesta
    message = create_new_message(session.session_id, data, db)

    return message


