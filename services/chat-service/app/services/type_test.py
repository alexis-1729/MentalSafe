from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import UUID4
import uuid
from app.schemas.type_test import *
from app.models import type_test as TypeTest


def create_type_test(data: type_test_create, db: Session):
    new = TypeTest(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def get_type_test_by_id(type_id: UUID4, db: Session)-> type_test_response | None:
    result = db.query(TypeTest).filter(TypeTest.typeT_id == type_id).first()
    if not result:
        return None
    return result

def get_type_test_by_name(name: str, db: Session)-> type_test_response | None:
    result = db.query(TypeTest).filter(TypeTest.name_test == name).first()
    if not result:
        return None
    return result.typeT_id
