from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from uuid import UUID
from app.schemas.profesional import profesionalCompleteResponse, profesionalCreate,startPoint, startPointResponse
from app.services.profesional import get_perfil, create_perfil
from app.schemas.security import TokenData
from app.services.security import verify_access_token
from app.services.calification import star

router = APIRouter(
    prefix = "/perfil",
    tags = ["Perfil Profesional"]
)

@router.post("/")
def create_profesional(
    data: profesionalCreate, 
    db: Session = Depends(get_db),
    # token_data: TokenData = Depends(verify_access_token)
    ):
    # if token_data.rol != "profesional":
    #     raise HTTPException(status_code ="401", detail = "Error de credenciales")
    
    return create_perfil(data, db)

@router.get("/profesional", response_model = profesionalCompleteResponse)
def get_profesional(
    id_pro: UUID, 
    db: Session = Depends(get_db)
    # token_data: TokenData = Depends(verify_access_token)
    ):
    # if token_data.sub != id_pro or token_data.rol != "profesional":
    #   raise HTTPException(status_code = 401, detail = "Credenciales invalidas")

    result = get_perfil(id_pro, db)
    if result is None:
        raise HTTPException(status_code = 404, detail = "No se encontro el perfil")
    return result


@router.post("/set_calification")
def set_calification(data: startPoint, 
                     db: Session = Depends(get_db),
                    #  token_data: TokenData = Depends(verify_access_token)
                     ):
    # if token_data.rol != "user":
    #     raise HTTPException(status_code = 401, detail = "Credenciales Invalidas")
    
    result =  star(data, db)
    if result is None:
        raise HTTPException(status_code = 404, detail = "not found calification")
    return result