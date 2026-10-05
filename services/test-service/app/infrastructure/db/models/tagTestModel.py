import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.infrastructure.db.database import Base

class TagTestModel(Base):
    __tablename__ = "tag_test"
    
    tag_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    id_test_type = Column(UUID(as_uuid=True), ForeignKey("type_test.typeT_id", ondelete="CASCADE"), nullable=False)

    # Relación con el tipo de test
    type = relationship("TypeTestModel", back_populates="tags")