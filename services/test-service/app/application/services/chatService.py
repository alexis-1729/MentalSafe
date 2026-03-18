import pickle
import os
from app.domain.entities.chat import Chat
from app.infrastructure.db.unit_of_work_impl import UnitOfWorkImpl
from app.api.schemas.chatSchemas import ChatCreate

class ChatService:
    def __init__(self, uow: UnitOfWorkImpl):
        self.uow = uow
        self.vectorizer_path = "app/infrastructure/ai_models/CountVectorizer.pkl"
        self.model_path = "app/infrastructure/ai_models/tu_otro_modelo.pkl" 
        
        self.vectorizer = self._load_pickle(self.vectorizer_path)
        self.classifier = self._load_pickle(self.model_path)

    def _load_pickle(self, path):
        if os.path.exists(path):
            with open(path, 'rb') as f:
                return pickle.load(f)
        return None

    def process_message(self, chat_data: ChatCreate) -> Chat:
        message_text = chat_data.message
        detected_intent = "desconocido"
        ai_response = "Lo siento, no pude procesar tu mensaje."

        if self.vectorizer and self.classifier:
            vector = self.vectorizer.transform([message_text])
            prediction = self.classifier.predict(vector)
            detected_intent = str(prediction[0])
            ai_response = f"He detectado que tu intención es: {detected_intent}"

        with self.uow:
            new_chat = Chat(
                id=None,
                user_id=chat_data.user_id,
                message=message_text,
                response=ai_response,
                intent=detected_intent
            )
            return self.uow.chats.save(new_chat)