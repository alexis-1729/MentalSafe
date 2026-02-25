from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app.models import type_test as TypeTestModel
from app.schemas.type_test import type_test_create, type_test_response
from app.services.type_test import *

router = APIRouter(
    prefix = "/type_test",
    tags=["Type Test"]
)

@router.post("/", response_model = type_test_response)
def create_type_test_route(data: type_test_create, db:Session = Depends(get_db)):
    return create_type_test(data, db)

@router.get("/", response_model = list[type_test_response])
def list_type_test(db:Session = Depends(get_db)):
    return db.query(TypeTestModel)

@router.get("/{typeT_id}", response_model = type_test_response)
def get_type_test(typeT_id: str, db: Session = Depends(get_db)):
    result = get_type_test_by_id(typeT_id)
    if(not result):
        raise HTTPException(status_code = 404, detail = "Type Test not found")
    return result