from sqlalchemy.orm import Session
from typing import List
from app.domain.repositories.chatRepository import ChatRepository
from app.infrastructure.db.models.chatModel import ChatModel
from app.infrastructure.db.mappers.chatMapper import ChatMapper
from app.domain.entities.chat import Chat

class ChatRepositoryImpl(ChatRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, chat: Chat) -> Chat:
        model = ChatMapper.to_model(chat)
        self.db.add(model)
        self.db.flush()
        return ChatMapper.to_entity(model)

    def find_by_user(self, user_id: int) -> List[Chat]:
        models = self.db.query(ChatModel).filter(ChatModel.user_id == user_id).all()
        return [ChatMapper.to_entity(m) for m in models]

    def find_all(self) -> List[Chat]:
        models = self.db.query(ChatModel).all()
        return [ChatMapper.to_entity(m) for m in models]