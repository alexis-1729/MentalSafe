from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.chat import Chat

class ChatRepository(ABC):
    @abstractmethod
    def save(self, chat: Chat) -> Chat:
        pass

    @abstractmethod
    def find_by_user(self, user_id: int) -> List[Chat]:
        pass

    @abstractmethod
    def find_all(self) -> List[Chat]:
        pass