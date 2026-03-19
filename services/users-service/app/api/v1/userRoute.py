from fastapi import APIRouter, Depends, status, HTTPException
from uuid import UUID
from app.api.schemas.userSchemas import UserCreate, UserResponse
from app.application.dependencies import get_user_service
from app.application.services.userService import UserService
from app.domain.exceptions import UserNotFound

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return await service.create_user(user_in)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    try:
        return await service.get_user_by_id(user_id)
    except UserNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.get("/by-auth/{id_auth}", response_model=UserResponse)
async def get_user_by_auth(id_auth: UUID, service: UserService = Depends(get_user_service)):
    try:
        return await service.get_user_by_id_auth(id_auth)
    except UserNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.get("/", response_model=list[UserResponse])
async def get_all_users(service: UserService = Depends(get_user_service)):
    return await service.get_all_users()