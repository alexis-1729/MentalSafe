from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, func, DateTime, Boolean
from datetime import datetime
from app.infrastructure.db.database import Base
import uuid

class RefreshTokenModel(Base):
    __tablename__ = "refreshToken"
    id: Mapped[uuid.UUID] = mapped_column(primary_key = True)
    auth_id: Mapped[uuid.UUID] = mapped_column( index = True)
    token_hash: Mapped[str] = mapped_column(String, unique = True)
    expires_at: Mapped[datetime] = mapped_column(DateTime)
    revoked: Mapped[bool] = mapped_column(Boolean, default = False)
