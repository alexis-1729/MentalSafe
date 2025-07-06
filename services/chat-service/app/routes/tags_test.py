from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import get_db
from ..database improt get_db
from ..models import tags_test as TagsTestModel
from ..schemas import tags_test_create, tags_test_response

router = APIRouter(
    prefix = "/tags_test",
    tags = "Tags test"
)

@router.post("/", response_model = tags_test_response)
def create_tags_test(data: tags_test_create, db:Session = Depends(get_db)):
    new_tag = TagsTestModel(**data.dict())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

@router.get("/", response_model = list[tags_test_response])
def list_tags(db:Session = Depends(get_db)):
    return db.query(TagsTestModel).all()

@router.get("/{tag_id}", response_model = tags_test_response)
def get_tag_by_id(tag_id: str, db:Session = Depends(get_db)):
    result = db.query(TagsTestModel).filter(TagsTestModel.tag_id == tag_id).first()

    if not tag:
        raise HTTPException(status_code = 404, detail="Tag not found")
    return result
