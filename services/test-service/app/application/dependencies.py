from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.db.database import get_db
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.application.services.chatService import ChatService

def get_chat_service(db: Session = Depends(get_db)):
    uow = UnitOfWorkImpl(db)
    return ChatService(uow)