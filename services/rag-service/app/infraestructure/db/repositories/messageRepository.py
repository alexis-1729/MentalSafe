from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from app.domain.repositories.messageRepository import MessageRepository
from app.domain.entities.message import Message
from app.infraestructure.db.models.messageModel import MessageORM
from app.infraestructure.db.mappers.messageMapper import MessageMapper
from uuid import UUID

class SQLAlchemyMessageRepository(MessageRepository):
    """Implementación del repositorio de mensajes usando SQLAlchemy"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.mapper = MessageMapper()

    async def add(self, message: Message) -> None:
        """Añadir un nuevo mensaje a la base de datos"""
        message_orm = self.mapper.to_orm(message)
        self.session.add(message_orm)
        await self.session.flush()

    async def get_by_session(self, session_id: UUID) -> list[Message] | None:
        """Obtener mensajes por lista de mensajes - Implementa la interfaz del dominio"""
                
        stmt = select(MessageORM).where(MessageORM.session_id == session_id)
        result = await self.session.execute(stmt)
        messages_orm = result.scalars().all()
        
        if not messages_orm:
            return None
        
        return [self.mapper.to_domain(msg_orm) for msg_orm in messages_orm]
