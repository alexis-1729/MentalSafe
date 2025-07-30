from app import models
from app.schemas.chat import ChatSessionCreate, ChatSessionResponse
from sqlalchemy.orm import Session
from app.models import ChatSessions
from datetime import datetime
import uuid

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
        created_at = new_session.created_at
    )
