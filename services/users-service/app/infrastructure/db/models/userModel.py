import uuid
from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.infrastructure.db.database import Base
from datetime import datetime

class UserModel(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_auth = Column(UUID(as_uuid=True), nullable=False, unique=True)
    full_name = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    fecha_nac = Column(Date, nullable=False)
    genero = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)