from fastapi import APIRouter
from app.api.v1 import chatRoute

api_router = APIRouter()
api_router.include_router(chatRoute.router, prefix="/chat", tags=["IA Chat"])