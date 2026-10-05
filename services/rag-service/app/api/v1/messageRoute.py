from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas.messageSchemas import ChatMessageCreate, ChatMessageResponse
from app.application.services.messageService import MessageService
from app.application.pipeline.flow import Pipeline
from app.application.dependencies import get_message_service, get_pipeline
from uuid import UUID

router = APIRouter()


@router.post("/", response_model=ChatMessageResponse)
async def create_message(
    data: ChatMessageCreate,
    service: MessageService = Depends(get_message_service),
    pipeline: Pipeline = Depends(get_pipeline)
):
    try:


        #---------------- Mensaje usuario -------

        await service.create_message(
            session_id=data.session_id,
            sender=data.sender,
            message=data.message,
            emotion_tag= "gg"
        )


        response = pipeline.pipeline(data.message)

        message = service.create_message(
            session_id= data.session_id,
            sender = "IA",
            message = response,
            emotion_tag = "gg"
        )


        return ChatMessageResponse(
            id_message=message.id_message,
            session_id=data.session_id,
            sender="IA",
            content=message.message,
            created_at= message.created_at
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating message: {str(e)}")


@router.get("/{session_id}", response_model=list[ChatMessageResponse])
async def get_messages_by_session(
    session_id: UUID,
    service: MessageService = Depends(get_message_service)
):
    try:
        messages = await service.get_messages(session_id)
        
        if not messages:
            raise HTTPException(status_code=404, detail="No messages found for this session")
        
        return [
            ChatMessageResponse(
                id_message=msg.id_message,
                session_id=msg.session_id,
                sender=msg.sender,
                content=msg.message,
                created_at=msg.created_at
            )
            for msg in messages
        ]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching messages: {str(e)}")
