from sqlalchemy import Column, String, DateTime, Integer, Text, ForeignKey
from sqlalchemy.sql import func
from app.infrastructure.db.database import Base

class ChatModel(Base):
    __tablename__ = "ia_chats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False) 
    message = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    intent = Column(String(50), nullable=True) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())