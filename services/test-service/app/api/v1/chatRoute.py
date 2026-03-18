from fastapi import APIRouter, Depends
from typing import List
from app.api.schemas.chatSchemas import ChatCreate, ChatResponse
from app.application.dependencies import get_chat_service
from app.application.services.chatService import ChatService

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def post_chat(chat_in: ChatCreate, service: ChatService = Depends(get_chat_service)):
    return service.process_message(chat_in)

@router.get("/history/{user_id}", response_model=List[ChatResponse])
def get_history(user_id: int, service: ChatService = Depends(get_chat_service)):
    return service.get_user_history(user_id)