from fastapi import APIRouter
from app.api.v1 import userRoute

api_router = APIRouter()
api_router.include_router(userRoute.router, prefix="/users", tags=["users"])