from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import result_test as ResultTestModel
from google.cloud import dialogflow_v2 as dialogflow
from .app.schemas import MessageRequest, result_test_create, result_test_response

router = APIRouter(
    prefix = "/test_result",  
    tags = ["Results"]
    )

@router.post("/", response_model = result_test_response)
def create_result_test(data:result_test_create, db:Session = Depends(get_db)):
    new_result = ResultTestModel(**data.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result

@router.get("/", response_model = list[result_test_response])
def list_result(db:Session = Depends(get_db)):
    return db.query(ResultTestModel).all()

@router.get("/{result_id}", response_model = result_test_response)
def get_result_by_id(result_id : str, db:Session = Depends[get_db]):
    result = db.query(ResultTestModel).filter(ResultTestModel.result_id == result_id).first()
    if not result:
        raise HTTPException(status_code = 404, detail = "Result not found")
    return result

