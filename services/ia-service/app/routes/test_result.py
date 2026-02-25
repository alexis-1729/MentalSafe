from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import result_test as ResultTestModel
from app.schemas.result_test import  result_test_create, result_test_response
from app.services.result_test import *

router = APIRouter(
    prefix = "/test_result",  
    tags = ["Results"]
    )

@router.post("/", response_model = result_test_response)
def create_result_test_route(data:result_test_create, db:Session = Depends(get_db)):
    return create_result_test(data, db)

@router.get("/", response_model = list[result_test_response])
def list_result(db:Session = Depends(get_db)):
    return db.query(ResultTestModel).all()

@router.get("/{result_id}", response_model = result_test_response)
def get_result_by_id(result_id : str, db:Session = Depends(get_db)):
    result = get_result_id(result_id, db)
    if not result:
        raise HTTPException(status_code = 404, detail = "Result not found")
    return result

