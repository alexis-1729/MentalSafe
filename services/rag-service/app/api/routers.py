from fastapi import APIRouter
from app.api.v1.messageRoute import router as message_router
from app.api.v1.sessionRoute import router as session_router

api_router_v1 = APIRouter(prefix="/api/v1")

api_router_v1.include_router(
    message_router,
    prefix="/message",
    tags=["Message"]
)

api_router_v1.include_router(
    session_router,
    prefix="/session",
    tags=["Session"]
)

router = APIRouter()

router.include_router(api_router_v1)
