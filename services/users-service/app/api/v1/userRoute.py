from fastapi import APIRouter, Depends, status
from app.api.schemas.userSchemas import UserCreate, UserResponse
from app.application.dependencies import get_user_service
from app.application.services.userService import UserService

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, service: UserService = Depends(get_user_service)):
    return service.register_user(user_in)