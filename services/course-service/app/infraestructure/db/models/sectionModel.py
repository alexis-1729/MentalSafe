from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy  import  ForeigKey
from app.infraestructure.database import Base
from typing import List
import uuid

class SectionORM(Base):
    __tablename__ = "section"
    
    id_section: Mapped[uuid.UUID] = mapped_column(primary_key = True, default = uuid.uuid4)
    id_course: Mapped[uuid.UUID] = mapped_column(UUID, ForeigKey("course.id_course", ondelete = "CASCADE"))

    course: Mapped["CourseORM"] = relationship("CourseORM", back_populates="sections")
    chapters: Mapped[List["Chapter"]] = relationship("ChapterORM", back_populates = "section", cascade = "all, delete-orphan")
    