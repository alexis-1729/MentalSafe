


from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import uuid
from sqlalchemy.sql import func
from datetime import datetime
Base = declarative_base()

class ChatSessions(Base):
    __tablename__ = "chat_sessions"
  
    id_session = Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    user_id = Column(UUID(as_uuid = True), nullable = False)
    title = Column(String(70), nullable=True)
    created_at = Column(DateTime, default = func.now())

    messages = relationship("ChatMessage", back_populates = "session", cascade = "all, delete-orphan")

class ChatMessage(Base):
    __tablename__ = "chat_message"

    id_message = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    session_id = Column(UUID(as_uuid = True), ForeignKey("chat_sessions.id_session"), nullable = False)
    sender = Column(String(30), nullable = True)
    message = Column(Text, nullable = False)
    emotion_tag = Column(String(70), nullable = False)
    created_at = Column(DateTime, default = func.now())

    session = relationship("ChatSessions", back_populates = "messages")
