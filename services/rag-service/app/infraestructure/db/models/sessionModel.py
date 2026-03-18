from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, String, Text, DateTime
from app.infraestructure.database import Base
from datetime import datetime
import uuid


class SessionORM(Base):
    __tablename__ = "sessions"

    id_session: Mapped[uuid.UUID] = mapped_column(primary_key = True)
    user_id: Mapped[uuid.UUID] = mapped_column(nullable = False)
    title: Mapped[uuid.UUID] = mapped_column(String(70), nullable = True)
    created_at: Mapped[datetime] = mapped_column(server_default = func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default = func.now(), onupdate = func.now())
    
    messages: Mapped["MessageORM"] = relationship("MessageORM", back_populates = "session")



