from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, String, Text, DateTime
from app.infraestructure.database import Base
from datetime import datetime
import uuid


class MessageORM(Base):
    __tablename__ = "message"

    id_message: Mapped[uuid.UUID] = mapped_column(primary_key = True)
    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sessions.id_session", ondelete = "CASCADE"))
    sender: Mapped[str] = mapped_column(String(30), nullable = True)
    message: Mapped[str] = mapped_column(Text, nullable = False)
    emotion_tag: Mapped[str] = mapped_column(Text, nullable = False)
    created_at: Mapped[datetime] = mapped_column(server_default = func.now())

    session: Mapped["SessionORM"] = relationship("SessionORM", back_populates = "messages")


