from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import UUID4
import uuid
from app.schemas.test_user import *
from app.models import test_user as TestUser
from app.database import get_db


def create_test_user(data: test_user_create, db: Session):
    new_result = TestUser(**data.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result

def get_test_user_by_userId(user_id: str, db: Session= Depends(get_db))->list[test_user_response] | None:
    result = db.query(TestUser).filter(TestUser.id_user == user_id).all()
    if not result:
        return None
    return result

def get_test_user_by_testId(test_id: UUID4, db: Session)-> test_user_create | None:
    result = db.query(TestUser).filter(TestUser.test_id == test_id).first()
    if not result:
        return None
    return result

