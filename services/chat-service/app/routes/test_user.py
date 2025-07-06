from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from .database import get_db
from .models import test_user as TestUserModel
from .schemas import test_user_create, test_user_response

router = APIRouter(
    prefix = "/test_user",
    tags=["Test User"]
)

@router.post("/", response_model = test_user_response)
def create_test_user(data: test_user_create, db:Session = Depends(get_db)):
    new_test = TestUserModel(**data.dict())
    db.add(new_test)
    db.commit()
    db.refresh(new_test)

@router.get("/", response_model = list[test_user_response])
def list_test_user(db:Session = Depends(get_db)):
    return  db.query(TestUserModel).all()

@router.get("/{test_id}", response_model = test_user_response)
def get_test_user_by_id(test_id: str, db: Session= Depends(get_db)):
    result = db.query(TestUserModel).filter(TestUserModel.test_id == test_id).first()
    if not result:
        raise HTTPException(status_code = 404, detail= "Test not found")
    return result