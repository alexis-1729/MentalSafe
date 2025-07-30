from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import ChatSessionCreate, ChatSessionResponse, ChatMessageResponse
from app.database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from app.models import *
from datetime import datetime
import uuid

router = APIRouter(prefix = "/chat/sessions/{user_id}", tags = ["message"])

# #CrearMensaje agregar conexion con modelo ia
# @router.post("/sessions/{session_id}/messages", response_model = ChatMessageResponse)
# def create_chat_message(session_id: UUID4, payload: ChatMessageCreate, 
#                         db: Session = Depends(get_db)):
#     #Verificacion de sesion existente
#     session_obj = db.query(ChatSessions).filter(ChatSessions.id_session == session_id).first()
#     if not session_obj:
#         raise HTTPException(status_code = 404, detail = "Session not found")
    
#     #Crear el mensaje
#     new_message = ChatMessage(
#         session_id = session_id,
#         sender = payload.sender,
#         content = payload.content, 
#     )

#     db.add(new_message)
#     db.commit()
#     db.refresh(new_message)

#     return new_message

#Listar Mensajes
@router.get("/sessions/{session_id}/messages", response_model = list[ChatMessageResponse])
def list_chat_messages(
                       session_id:str,
                       db:Session = Depends(get_db),
                       skip: int = 0,
                       limit: int = 50,
                       ):
    #verificar que la sesion existe
    session_obj = db.query(ChatSession).filter(ChatSessions.id_session == session_id).first()
    if not session_obj:
        raise HTTPException(status_code = 404, detail = "Session not found")
    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.asc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return messages 