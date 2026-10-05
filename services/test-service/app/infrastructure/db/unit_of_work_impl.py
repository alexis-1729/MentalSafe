from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.unit_of_work import IUnitOfWork
from app.infrastructure.db.repositories import (
    TypeTestRepository,
    ResultTestRepository,
    TagTestRepository,
    TestUserRepository,
)


class UnitOfWorkImpl(IUnitOfWork):
    """Implementación del Unit of Work para de la infraestructura"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.type_test = TypeTestRepository(session)
        self.result_test = ResultTestRepository(session)
        self.tag_test = TagTestRepository(session)
        self.test_user = TestUserRepository(session)

    async def begin(self) -> None:
        """Inicia una transacción"""
        await self.session.begin()

    async def commit(self) -> None:
        """Confirma la transacción"""
        await self.session.commit()

    async def rollback(self) -> None:
        """Revierte la transacción"""
        await self.session.rollback()

    async def close(self) -> None:
        """Cierra la conexión"""
        await self.session.close()