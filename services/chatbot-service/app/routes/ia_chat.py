from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import *
from sqlalchemy.orm import Session
from app.services.ia_sessions import *
from app.services.ia_messages import *
from app.database import get_db
import uuid
from datetime import datetime, timedelta

router = APIRouter(
    prefix = "/chating",
    tags = ["Chating"]
)

TIMEOUT = 30

@router.post("/{user_id}")
def init_chat(user_id: str, data: ChatMessageCreate,db: Session = Depends(get_db)):
     #obtener hora actual 
    now = datetime.utcnow()

    last = get_session_by_id(user_id, db)

    if(last):
        if(now - last.updated_at < timedelta(minutes=TIMEOUT)):
            session = last

        else: 
            session_actual = ChatSessionCreate(
            user_id=user_id,
            title = "NEW"
            )

            #creamos sesion
            session = create_new_session(session_actual, db)
    else: 
         session_actual = ChatSessionCreate(
            user_id=user_id,
            title = "NEW"
            )

         #creamos sesion
         session = create_new_session(session_actual, db)
    
    
    #creamos mensaje y recibimos respuesta
    message = create_new_message(session.session_id, data, db)

    return message


