import uuid
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.infrastructure.database import Base

class ResultTestModel(Base):
    __tablename__ = "test_results"
    
    result_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    score = Column(Integer, nullable=False)
    id_test = Column(UUID(as_uuid=True), ForeignKey("type_test.typeT_id", ondelete="CASCADE"), nullable=False)
    
    # Relaciones
    test = relationship("TypeTestModel", back_populates="results")
    test_users = relationship("TestUserModel", back_populates="result", cascade="all, delete")