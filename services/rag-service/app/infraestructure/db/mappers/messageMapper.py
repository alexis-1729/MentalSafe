from app.domain.entities.message import Message
from app.infraestructure.db.models.messageModel import MessageORM
import uuid

class MessageMapper:

    @staticmethod
    def to_domain(orm: MessageORM) -> Message:
        return Message(
            id_meesage=orm.id_message,
            session_id=orm.session_id,
            sender=orm.sender,
            message=orm.message,
            emotion_tag=orm.emotion_tag,
            created_at=orm.created_at
        )
    
    @staticmethod
    def to_orm(entity: Message) -> MessageORM:
        return MessageORM(
            id_message=entity.id_message,
            session_id=entity.session_id,
            sender=entity.sender,
            message=entity.message,
            emotion_tag=entity.emotion_tag
        )
