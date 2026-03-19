from abc import ABC, abstractmethod
from app.domain.repositories import (
    ITypeTestRepository,
    IResultTestRepository,
    ITagTestRepository,
    ITestUserRepository,
)


class IUnitOfWork(ABC):
    """Interfaz del Unit of Work para manejar transacciones"""

    type_test: ITypeTestRepository
    result_test: IResultTestRepository
    tag_test: ITagTestRepository
    test_user: ITestUserRepository

    @abstractmethod
    async def begin(self) -> None:
        """Inicia una transacción"""
        pass

    @abstractmethod
    async def commit(self) -> None:
        """Confirma la transacción"""
        pass

    @abstractmethod
    async def rollback(self) -> None:
        """Revierte la transacción"""
        pass

    @abstractmethod
    async def close(self) -> None:
        """Cierra la conexión"""
        pass
