from fastapi import APIRouter, Depends, status
from app.api.schemas.test_schemas import TestUserCreate, TestUserResponse
from app.application.dependencies import get_test_user_service
from app.application.services.test_user_service import TestUserService

router = APIRouter()

@router.post("/register", response_model=TestUserResponse, status_code=status.HTTP_201_CREATED)
async def register_user_test(data: TestUserCreate, service: TestUserService = Depends(get_test_user_service)):
    return await service.create_test_user(data) # Asumiendo que el método se llama así en tu service