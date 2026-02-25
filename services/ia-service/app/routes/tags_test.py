from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from  app.models import tags_test as TagsTestModel
from app.schemas.tags_test import tags_test_create, tags_test_response
from app.services.tags_test import *
router = APIRouter(
    prefix = "/tags_test",
    tags = ["Tags test"]
)

@router.post("/", response_model = tags_test_response)
def create_tags_test(data: tags_test_create, db:Session = Depends(get_db)):
    return create_tags_test(data, db)

@router.get("/", response_model = list[tags_test_response])
def list_tags(db:Session = Depends(get_db)):
    return db.query(TagsTestModel).all()

@router.get("/{tag_id}", response_model = tags_test_response)
def get_tag_by_id(tag_id: str, db:Session = Depends(get_db)):
    result = get_tag_id(tag_id, db)
    if not result:
        raise HTTPException(status_code = 404, detail="Tag not found")
    return result
