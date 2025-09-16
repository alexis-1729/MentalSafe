from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base


class user_auth(Base):
    __tablename__ = "user_auth"
    id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    username = Column(String, unique = True, index = True)
    password_h = Column(String, nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    role = Column(String, nullable = False)

class token_auth(Base):
    __tablename__ = "token_auth"
    jti= Column(UUID(as_uuid = True), primary_key= True, nullable = False)
    sub = Column(String, nullable = False)
    exp = Column(String, nullable = False)

    