from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import UUID4
import uuid
from app.schemas.result_test import *
from app.models import result_test as ResultTestModel


def create_result_test(data: result_test_create, db: Session):
    new_result = ResultTestModel(**data.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result


def get_result_id(result_id: UUID4, db: Session)-> result_test_response | None:
    result = db.query(ResultTestModel).filter(ResultTestModel.result_id == result_id).first()
    if not result:
        return None
    return result