from uuid import UUID, uuid4
from app.domain.unit_of_work import UnitOfWork
from app.domain.entities.message import Message


class MessageService:
    """Servicio para gestionar operaciones con mensajes"""

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_message(
        self,
        session_id: UUID,
        sender: str,
        message: str,
        emotion_tag: str,
        message_id: UUID | None = None
    ) -> Message:
        """Crear un nuevo mensaje"""
        if message_id is None:
            message_id = uuid4()

        new_message = Message(
            id_meesage=message_id,
            session_id=session_id,
            sender=sender,
            message=message,
            emotion_tag=emotion_tag
        )

        async with self.uow as uow:
            await uow.messages.add(new_message)
            await uow.commit()

        return new_message

    async def get_messages(self, session_id: UUID) -> list[Message] | None:
        """Obtener múltiples mensajes"""
        if not session_id:
            return None

        async with self.uow as uow:
            return await uow.messages.get_by_session(session_id)

    # async def get_message(self, message: Message) -> Message | None:
    #     """Obtener un mensaje específico"""
    #     async with self.uow as uow:
    #         return await uow.messages.get([message])
