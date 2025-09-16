from sqlalchemy.orm import Session
from pydantic import UUID4
from uuid import UUID
from app.schemas.course import courseResponse
from app.schemas.chapter import chapterResponse
from app.models import course as courseModel, section, chapter, content

def get_course_id(id_course: UUID,db: Session)-> courseResponse | None:
    ans = db.query(courseModel).filter(courseModel.id_course == id_course).first()
    if(not ans):
        return None
    return ans

def get_course_tag(tag: str, db: Session)-> courseResponse | None:
    result = db.query(courseModel).filter(courseModel.tag == tag).first()
    return result

def get_list_course(db: Session):
    return db.query(courseModel).all()

def get_chapter(id_curso: UUID, db: Session) -> chapterResponse | None:
    sect = db.query(section).filter(section.id_cours == id_curso).first()
    if not sect:
        return None
    chaps = db.query(chapter).filter(chapter.id_sect == sect.id_section).all()
    if not chaps:
        return None
    return chaps

def get_content(id_chapter: UUID, db: Session):
    try:
        result = db.query(content).filter(content.id_chap == id_chapter).first()
        if not result:
            return None
        return result
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Error en la base de datos: {str(e.orig)}")