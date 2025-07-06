from fastapi import APIRouter, Depends, HTTPException
from app import models
from app.schemas.chat import ChatSessionCreate, ChatSessionResponse
from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from .models import ChatSession
from datetime import datetime
import uuid

router = APIRouter(prefix = "/chat/sessions/{user_id}", tags = ["message"])

#CrearMensaje agregar conexion con modelo ia
@router2.post("/sessions/{session_id}/messages", response_model = ChatMessageResponse)
def create_chat_message(session_id: UUID, payload: ChatMessageCreate, 
                        db: Session = Depends(get_db)):
    #Verificacion de sesion existente
    session_obj = db.query(ChatSessions).filter(ChatSessions.id_session == session_id).first()
    if not session_obj:
        raise HTTPException(status_code = 404, detail = "Session not found")
    
    #Crear el mensaje
    new_message = ChatMessage(
        session_id = session_id,
        sender = payload.sender,
        content = payload.content, 
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message

#Listar Mensajes
@router2.get("/sessions/{session_id}/messages", response_model = List[ChatMessageResponse])
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
        .filter(ChatMessage.session_id = session_id)
        .order_by(ChatMessage.created_at.asc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return messages 