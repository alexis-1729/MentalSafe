
from sqlalchemy.orm import Session
from app.models import course as Course, section, chapter, content
import logging
from app.schemas.course import courseCreate, courseResponse
from app.schemas.section import sectionCreate, sectionResponse
from app.schemas.chapter import chapterCreate, chapterResponse
from app.schemas.content import contentCreate, contentResponse
from uuid import UUID

class CourseData:
    def __init__(self, db: Session):
        self.db = db
        self.logger = logging.getLogger("CourseData")

    def createCourse(self, course: courseCreate)-> courseResponse | None:
        try:
            self.logger.info(f"Creating course")
            new_course = Course(**course.dict())
            self.db.add(new_course)
            self.db.commit()
            self.db.refresh(new_course)
            return new_course
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Error creating course: {e}")

    def createSection(self, sect: sectionCreate)-> sectionResponse | None:
        try:
            new = section(**sect.dict())
            self.db.add(new)
            self.db.commit()
            self.db.refresh(new)
            return new
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Error creating section {e}")
            return None
    
    def createChapter(self, chapt: chapterCreate) -> chapterResponse | None:
        try:
            new = chapter(**chapt.dict())
            self.db.add(new)
            self.db.commit()
            self.db.refresh(new)
            return new
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Error creating chapter {e}")
            return None
    
    def createContent(self, cont: contentResponse):
        try:
            new = content(**cont.dict())
            self.db.add(new)
            self.db.commit()
            self.db.refresh(new)
            return new
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Error creating content {e}")
            return None



    