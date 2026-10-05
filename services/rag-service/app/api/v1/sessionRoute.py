from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas.sessionSchemas import ChatSessionCreate, ChatSessionResponse
from app.application.services.sessionService import SessionService
from app.application.dependencies import get_session_service
from uuid import UUID

router = APIRouter()


@router.post("/", response_model=ChatSessionResponse)
async def create_session(
    data: ChatSessionCreate,
    service: SessionService = Depends(get_session_service)
):
    try:
        session = await service.create_session(
            user_id=data.user_id,
            title=data.title or f"Session for user {data.user_id}"
        )

        return ChatSessionResponse(
            session_id=session.id_session,
            created_at=session.created_at,
            updated_at=session.updated_at
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating session: {str(e)}")


@router.get("/{user_id}", response_model=ChatSessionResponse)
async def get_session(
    user_id: UUID,
    service: SessionService = Depends(get_session_service)
):
    try:
        session = await service.get_session(user_id)
        
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        return ChatSessionResponse(
            session_id=session.id_session,
            created_at=session.created_at,
            updated_at=session.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching session: {str(e)}")


@router.put("/{user_id}", response_model=ChatSessionResponse)
async def update_session(
    user_id: UUID,
    data: ChatSessionCreate,
    service: SessionService = Depends(get_session_service)
):
    try:
        session = await service.update_session(
            user_id=user_id,
            title=data.title or f"Updated session for user {user_id}"
        )

        return ChatSessionResponse(
            session_id=session.id_session,
            created_at=session.created_at,
            updated_at=session.updated_at
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating session: {str(e)}")
