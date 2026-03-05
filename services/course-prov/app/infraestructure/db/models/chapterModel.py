from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy  import  ForeigKey, String, Boolean
from app.infraestructure.database import Base
from typing import List
import uuid

class ChapterORM(Base):
    __tablename__ = "chapter"

    id_chapter: Mapped[uuid.UUID] = mapped_column(primary_key = True, default = uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable = False)
    description: Mapped[str] = mapped_column(String, nullable = False)
    num_caps: Mapped[str] = mapped_column(String(10))
    duration: Mapped[str] = mapped_column(String)
    numero: Mapped[int | None] = mapped_column(nullable = True)
    id_section: Mapped[uuid.UUID] = mapped_column(UUID, ForeigKey("section.id_section", ondelete ="CASCADE"))
    complete: Mapped[bool] = mapped_column(Boolean, default = False)
    url_image: Mapped[int | None] = mapped_column(String,nullable = True)

    section: Mapped["SectionORM"] = relationship("SectionORM", back_populates = "chapters")
    contents: Mapped[List["ContentORM"]] = relationship("ContentORM", back_populates = "chapter", cascade="all, delete-orphan")
       