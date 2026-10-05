from uuid import UUID, uuid4
from app.domain.unit_of_work import UnitOfWork
from app.domain.entities.session import Session


class SessionService:
    """Servicio para gestionar operaciones con sesiones"""

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_session(
        self,
        user_id: UUID,
        title: str,
        session_id: UUID | None = None
    ) -> Session:
        """Crear una nueva sesión"""
        if session_id is None:
            session_id = uuid4()

        new_session = Session(
            id_session=session_id,
            user_id=user_id,
            title=title
        )

        async with self.uow as uow:
            await uow.sessions.add(new_session)
            await uow.commit()

        return new_session

    async def get_session(self, user_id: UUID) -> Session | None:
        """Obtener una sesión"""
        async with self.uow as uow:
            return await uow.sessions.get(user_id)

    async def update_session(
        self,
        user_id: UUID,
        title: str
    ) -> Session:
        """Actualizar una sesión"""
        updated_session = Session(
            user_id=user_id,
            title=title
        )

        async with self.uow as uow:
            await uow.sessions.add(updated_session)
            await uow.commit()

        return updated_session

    # async def delete_session(self, session: Session) -> None:
    #     """Eliminar una sesión"""
    #     async with self.uow as uow:
    #         # Primero obtenemos la sesión para obtener su ID
    #         existing_session = await uow.sessions.get(session)
    #         if existing_session:
    #             # Aquí podrías implementar un método delete en el repositorio
    #             # Por ahora solo removemos de la sesión
    #             await uow.commit()
