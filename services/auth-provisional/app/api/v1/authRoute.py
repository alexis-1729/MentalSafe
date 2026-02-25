from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from app.api.schemas.authSchemas import UserCreate, UserResponse, UserLogin
from app.application.services.authService import AuthService
from app.application.dependencies import get_auth_service
from app.domain.exceptions import UserAlredyExists

router = APIRouter()


@router.post("/", response_model = UserResponse)
async def createUser(
    data: UserCreate,
    service: AuthService = Depends(get_auth_service)
):
    try:
        auth = await service.register(
            email=data.email,
            password_h=data.password_h,
            role=data.role
        )

        return UserResponse(
            id=auth.id,
            email=auth.email,
            role= auth.role
        )
    except UserAlredyExists:
        raise HTTPException(
            status_code = 409,
            detail = "User alredy exists"
        )
    
@router.get("{user_id}", response_model = UserResponse)
async def login(
    data: UserLogin,
    service: AuthService = Depends(get_auth_service)
):
    auth = await service.login(data.email, data.password_h)
    if not auth:
        raise HTTPException(status_code = 404, detail = "ID not found")
    return auth