from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy  import String
from app.infraestructure.database import Base
from typing import List
import uuid

class CourseORM(Base):
    __tablename__ ="course"

    id_course:Mapped[uuid.UUID] = mapped_column(primary_key = True, default = uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable = False)
    description: Mapped[str] = mapped_column(String)
    tag: Mapped[str] = mapped_column(String)
    url_image: Mapped[str] = mapped_column(String)

    sections = Mapped[List["SectionORM"]] = relationship("SectionORM", back_populates= "course", cascade = "all, delete-orphan")