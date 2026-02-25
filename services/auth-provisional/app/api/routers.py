from fastapi import APIRouter
from app.api.v1.authRoute import router

api_router_v1 = APIRouter(
    prefix = "/api/v1"
)

api_router_v1.include_router(
    router,
    prefix = "/auth",
    tags = ["Auth"]
)

router = APIRouter()

router.include_router(api_router_v1)