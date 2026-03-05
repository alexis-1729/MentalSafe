from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy  import  ForeigKey, String, Boolean
from app.infraestructure.database import Base
from typing import List
import uuid

class ContentORM(Base):
    __tablename__ = "content"

    id_content: Mapped[uuid.UUID]= mapped_column(primary_key = True, default = uuid.uuid4)
    content: Mapped[str] = mapped_column(String, nullable = False)
    url_video: Mapped[str | None] = mapped_column(String, nullable = True)
    complete: Mapped[bool] = mapped_column(Boolean, default = False)
    id_chapter: Mapped[uuid.UUID] = mapped_column(UUID, ForeigKey("chapter.id_chapter", ondelete = "CASCADE"))

    chapter: Mapped["ChapterORM"] = relationship("ChapterORM", back_populates = "contents")