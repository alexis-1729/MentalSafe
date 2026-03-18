from app.domain.entities.chat import Chat
from app.infrastructure.db.models.chatModel import ChatModel

class ChatMapper:
    @staticmethod
    def to_entity(model: ChatModel) -> Chat:
        if not model: return None
        return Chat(
            id=model.id,
            user_id=model.user_id,
            message=model.message,
            response=model.response,
            intent=model.intent,
            created_at=model.created_at
        )

    @staticmethod
    def to_model(entity: Chat) -> ChatModel:
        return ChatModel(
            id=entity.id,
            user_id=entity.user_id,
            message=entity.message,
            response=entity.response,
            intent=entity.intent
        )