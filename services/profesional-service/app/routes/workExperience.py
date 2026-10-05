from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.workExperience import workExperienceResponse, workExperienceCreate
from app.schemas.experienceData import experienceDataCreate, experienceDataResponse
from app.services.workExperience import get_experience, create_data, create_experience
from app.schemas.security import TokenData
from app.services.security import verify_access_token


router = APIRouter(
    prefix = "/experience",
    tags = ["Experiencia"]
)

@router.post("/")
def create_experience_route(
    id_pro: UUID, 
    data: experienceDataCreate, 
    db: Session = Depends(get_db),
    # token_data: TokenData = Depends(verify_access_token)
    ):
    # creamos los datos de experiencia
    result = create_data(data, db)
    # creamos el registro en la tabla de conexion con profesional
    ans = create_experience(
        workExperienceCreate(
            
             id_pro = id_pro,
             id_experience_data = result.id_data
           
        ), db
    )

    if ans.detail == None:
        raise HTTPException(status_code = 404, detail = "No se pudo crear la exp {ans.msg}")
    return ans


@router.get("/", response_model = list[experienceDataResponse])
def get_experiencia(
    id_pro: UUID, 
    db:Session = Depends(get_db),
    # token_data: TokenData = Depends(verify_access_token)
    ):
    
    result = get_experience(id_pro, db)
    if result is None:
        raise HTTPException(status_code = 404, detail = "No se encontro experiencia")
    return result
