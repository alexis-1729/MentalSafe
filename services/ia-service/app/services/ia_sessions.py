from app import models
from app.schemas.chat import ChatSessionCreate, ChatSessionResponse
from sqlalchemy.orm import Session
from app.models import ChatSessions
from datetime import datetime
import uuid

def get_session_by_id(user_id: str, db: Session)-> ChatSessionResponse:
    last_session = (
        db.query(ChatSessions)
        .filter(ChatSessions.user_id == user_id)
        .order_by(ChatSessions.created_at.desc())
        .first()
    )
    if last_session is None:
        return None

    return ChatSessionResponse(
        session_id = last_session.id_session,
        created_at = last_session.created_at,
        updated_at= last_session.updated_at
    )

def create_new_session(payload: ChatSessionCreate, db: Session ):
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
        created_at = new_session.created_at,
        updated_at= new_session.updated_at
    )
