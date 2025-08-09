from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.recomendation_test import RecomendationResponse
from app.services.recomendation_test import recomendationTest 
from pydantic import  UUID4

router = APIRouter(
    prefix = "/recomendation",
    tags = ["Recomendacion test"]
)

@router.post("/test/{user_id}", response_model = RecomendationResponse)
def get_receomendation(user_id: UUID4, db: Session = Depends(get_db)):
    return recomendationTest(user_id, db)
    