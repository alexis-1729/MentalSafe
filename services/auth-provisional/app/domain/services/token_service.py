from abc import ABC, abstractmethod
from uuid import UUID

class TokenService(ABC):

    @abstractmethod
    def generate_access(self, user_id: UUID)-> str:
        pass

    @abstractmethod
    def generate_refresh(self, user_id: UUID)-> str:
        pass

    @abstractmethod
    def verify(self, token: str)-> UUID:
        pass