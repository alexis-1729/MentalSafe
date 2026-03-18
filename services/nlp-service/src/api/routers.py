from fastapi import APIRouter
from src.api.v1.nlpRoute import router

api_v1_router = APIRouter(
    prefix = "/api/v1"
)

api_v1_router.include_router(
    router,
    prefix = "/predictor",
    tags = ["Prediction"]
)

app_router = APIRouter()

app_router.include_router(api_v1_router)