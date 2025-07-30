from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app.models import test_user as TestUserModel
from app.schemas.test_user import test_user_create, test_user_response

router = APIRouter(
    prefix = "/test_user",
    tags=["Test User"]
)

@router.post("/", response_model = test_user_response)
def create_test_user_route(data: test_user_create, db:Session = Depends(get_db)):
   return create_test_user(data, db)

@router.get("/", response_model = list[test_user_response])
def list_test_user(db:Session = Depends(get_db)):
    return  db.query(TestUserModel).all()

@router.get("/{test_id}", response_model = test_user_response)
def get_test_testId(test_id: str, db: Session= Depends(get_db)):
    result = get_test_user_by_testId(data, db)
    if  result is None:
        raise HTTPException(status_code = 404, detail= "Test not found")
    return result
