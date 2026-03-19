from sqlalchemy import Column, String, DateTime, Date
from sqlalchemy.sql import func
from app.infrastructure.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid = True), primary_key=True, default = uuid.uuid4)
    id_auth = Column(UUID(as_uuid = True), nullable = True, unique = True)
    full_name = Column(String(40), nullable = False)
    apellidos = Column(String(100), nullable= False)
    fecha_nac = Column(Date, nullable = False)
    genero = Column(String(30), nullable = False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())