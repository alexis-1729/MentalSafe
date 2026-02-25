from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, func, Datetime
from datetime import datetime
from app.infrastructure.db.database import Base

class AuthORM(Base):
    __tablename__ = "auth"

    id: Mapped[UUID] = mapped_column(primary_ey = True)
    email: Mapped[str] = mapped_column(String, unique = True)
    password_h: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(server_default = func.now())