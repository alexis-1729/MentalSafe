import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.infrastructure.db.database import Base

class TypeTestModel(Base):
    __tablename__ = "type_test"
    
    typeT_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_test = Column(String, nullable=False)
    num_q = Column(Integer, nullable=False)
    
    # Relaciones
    results = relationship("ResultTestModel", back_populates="test", cascade="all, delete")
    tags = relationship("TagTestModel", back_populates="type", cascade="all, delete")