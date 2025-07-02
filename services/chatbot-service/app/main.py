from fastapi import FastAPI, HTTPException, Depends, APIRouter, Query
from pydantic import BaseModel

from sqlalchemy.orm import declarative_base, relationship, Session

from app.schemas.chat import ChatSessionCreate, ChatSessionResponse
from app.database import SessionLocal, engine, get_db

import google.generativeai as genai
from dotenv import load_dotenv
from app import models
from app.models import ChatSessions
import uuid
from datetime import datetime
import os


#
router = APIRouter(prefix = "/chat", tags = ["Chat"])

#Cargar variables de entorno
load_dotenv()

#Inicializar clave de API de Google
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Crear las tablas
models.Base.metadata.create_all(bind=engine)

#Inicializar 
app = FastAPI()

#Endpoint crear sesiones
@router.post("/sessions/", response_model = ChatSessionResponse)
def create_chat_session(payload: ChatSessionCreate, db:Session = Depends(get_db)):
    #Crear session
    new_session = ChatSessions(
        id_session = uuid.uuid4(),
        user_id = payload.user_id,
        title = payload.title,
        created_at = datetime.utcnow()
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return ChatSessionResponse(
        session_id = new_session.id_session,
        created_at = new_session.created_at
    )

#listar sessiones de user --no probado
@router.get("/sessions/{user_id}", response_model = List[ChatSessionResponse])
def list_chat_sessions(user_id: str, 
                       db:Session = Depends(get_db),
                       skip: int = Query(0, ge = 0, description = "20"),
                       limit: int = Query(10, ge = 1, le = 100, description = "7"),
                       ):

    sessions = db.query(ChatSessions).filter(ChatSessions.user_id == user_id)
    .order_by(ChatSessions.created_at.desc())
    .offset(skip)
    .limit(limit)
    .all()
    return[
        ChatSessionResponse(
            session_id = s.session_id,
            created_at = s.created_at
        )
        for s in sessions
    ]

#Eliminar sesion
@router.delete("sessions/{session_id}")
def delete_chat_session(session_id: str, db: Session = Depends(get_db)):
    session_obj = db.query(ChatSessions).filter(ChatSessions.session_id == session_id).first()
    if not session_obj:
        raise HTTPException(status_code = 404, detail = "Session not found")
    
    db.delete(session_obj)
    db.commit()

    return {"message": f"Session  {session_id} deleted successfully"}

#CrearMensaje agregar conexion con modelo ia
@router.post("/sessions/{session_id}/messages", response_model = ChatMessageResponse)
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
@router.get("/sessions/{session_id}/messages", response_model = List[ChatMessageResponse])
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

#
app.include_router(router)

 


