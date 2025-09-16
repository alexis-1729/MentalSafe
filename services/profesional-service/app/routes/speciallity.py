from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from uuid import UUID
from app.schemas.especiallityData import speciallityResponse, speciallityCreate
from app.schemas.especiallity import profesionalSpResponse, profesionSpCreate
from app.services.speciallity import get_speciallity, create_data, create_speciallity
from app.schemas.security import TokenData
from app.services.security import verify_access_token
router = APIRouter(
    prefix = "/speciallity",
    tags = ["Especialidad y Certificaciones"]
)

@router.post("/")
def create_speciallity_route(
    id_pro: UUID, 
    data: speciallityCreate, 
    db: Session = Depends(get_db),
    # token_data: TokenData = Depends(verify_access_token)
    ):
    result = create_data(data, db)
    
    ans = create_speciallity(
        profesionSpCreate(
            id_pro=id_pro,
            id_speciallity= result.id_speciallity 
        ), db
    )
    if ans:
        return {"status":"success", "msg":"Se realizo la operacion exitosamente"}
    return {"status":"error", "msg":"No se realizo la operacion "}
   
    




@router.get("/", response_model = list[speciallityResponse])
def get_speciallity_route(
    id_pro: UUID, 
    db: Session = Depends(get_db),
    # token_data: TokenData = Depends(verify_access_token)
    ):
    ans = get_speciallity(id_pro, db)
    if ans is None:
        raise HTTPException(status_code = 404, detail = "No se econtraron especialidades")
    return ans