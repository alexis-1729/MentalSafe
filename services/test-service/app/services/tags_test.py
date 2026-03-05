from fastapi import APIRouter
from sqlalchemy.orm import Session
from pydantic import UUID4
import uuid
from app.schemas.tags_test import *
from app.models import tags_test as TagsTest


def create_tags_test(data: tags_test_create, db: Session)->tags_test_response:
    new = TagsTest(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def get_tag_id(tag_id: UUID4, db: Session)-> tags_test_response | None:
    result = db.query(TagsTest).filter(TagsTest.tag_id == tag_id).first()
    if not result:
        return None 
    return result