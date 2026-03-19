import uuid
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.infrastructure.db.database import Base

class TestUserModel(Base):
    __tablename__ = "test_user"
    
    test_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_user = Column(UUID(as_uuid=True), nullable=False) # ID que viene del microservicio de usuarios
    result_id = Column(UUID(as_uuid=True), ForeignKey("test_results.result_id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relación con el resultado
    result = relationship("ResultTestModel", back_populates="test_users")