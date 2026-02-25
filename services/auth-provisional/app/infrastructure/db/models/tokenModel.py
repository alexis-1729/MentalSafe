from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, func, Datetime, Boolean
from datetime import datetime
from app.infrastructure.db.database import Base


class RefreshTokenModel(Base):
    __tablename__ = "refreshToken"
    id: Mapped[UUID] = mapped_column(primary_key = True)
    auth_id: Mapped[UUID] = mapped_column(UUID, index = True)
    token_hash: Mapped[str] = mapped_column(String, unique = True)
    expires_at: Mapped[datetime] = mapped_column(Datetime)
    revoked: Mapped[bool] = mapped_column(Boolean, default = False)
