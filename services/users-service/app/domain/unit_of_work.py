from abc import abstractmethod, ABC
from app.domain.repositories.userRepository import UserRepository


class AbstractUnitOfWork(ABC):
    users: UserRepository

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        pass
    
    @abstractmethod
    async def rollback(self):
        pass
