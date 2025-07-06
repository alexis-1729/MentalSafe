from fastapi import APIRouter, Depends, HTTPException
from app import models
from app.schemas.chat import ChatSessionCreate, ChatSessionResponse
from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from .models import ChatSession
from datetime import datetime
import uuid

router = APIRouter(prefix = "/chat", tags = ["Sessions"])


#Endpoint crear sesiones
@router1.post("/sessions/", response_model = ChatSessionResponse)
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
@router1.get("/sessions/{user_id}", response_model = List[ChatSessionResponse])
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
@router1.delete("sessions/{session_id}")
def delete_chat_session(session_id: str, db: Session = Depends(get_db)):
    session_obj = db.query(ChatSessions).filter(ChatSessions.session_id == session_id).first()
    if not session_obj:
        raise HTTPException(status_code = 404, detail = "Session not found")
    
    db.delete(session_obj)
    db.commit()

    return {"message": f"Session  {session_id} deleted successfully"}