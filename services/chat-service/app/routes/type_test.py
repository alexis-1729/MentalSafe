from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from .database import get_db
from .models import type_test as TypeTestModel
from .schemas import type_test_create, type_test_response

router = APIRouter(
    prefix = "/type_test",
    tags=["Type Test"]
)

@router.post("/", response_model = type_test_response)
def create_type_test(data: type_test_create, db:Session = Depends(get_db)):
    new_type = TypeTestModel(**data.dict())
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    return new_type

@router.get("/", response_model = list[type_test_response])
def list_type_test(db:Session = Depends(get_db)):
    return db.query(TypeTestModel)

@router.get("/{typeT_id}", response_model = type_test_response)
def get_type_test(typeT_id: str, response_model = type_test_response):
    result = db.query(TypeTestModel).filter(TypeTestModel.typeT_id == typeT_id).first()
    if(not result):
        raise HTTPException(status_code = 404, detail = "Type Test not found")
    return result