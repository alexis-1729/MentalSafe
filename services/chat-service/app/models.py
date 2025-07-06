from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class test_user(Base):
    __tablename__ = "test_user"
    test_id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    id_user = Column(UUID(as_uuid = True), nullable =False)
    result_id= Column(UUID(as_uuid = True), ForeignKey("test_results.result_id", ondelete = "CASCADE"), nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())

    result = relatioship("result_test", back_populates = "test_users")

class tags_test(Base):
    __tablename__ = "tag_test"
    tag_id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name = Column(String, nullable = False)
    id_test_type = Column(UUID(as_uuid =  True), ForeignKey("type_test.typeT_id", ondelete = "CASCADE"), nullable = False)

    #relacion 
    type = relatioship("type_test", back_populates = "tags")
    
    #relacion inversa
    results = relatioship("result_test", back_populates = "tag", cascade = "all, delete")

class type_test(Base):
    __tablename__ = "type_test"
    typeT_id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name_test = Column(String, nullable = False)
    num_q = Column(Integer, nullable = False)

    #relacion
    tags = relatioship("tags_test", back_populates = "type", cascade = "all, delete")

class result_test(Base):
    __tablename__ = "test_results"
    result_id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    score = Column(Integer, nullable = False)
    id_tag = Column(UUID(as_uuid = True), ForeignKey("tag_test.tag_id", ondelete = "CASCADE"), nullable = False)

    tag = relatioship("tags_test", back_populates = "results")

    #relacion inversa
    test_users = relatioship("test_user", back_populates = "result", cascade = "all, delete")

