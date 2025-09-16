from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import uuid
from .database import Base

class course(Base):
    __tablename__ = "course"
    id_course = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    tag = Column(String, nullable = False)
    url_image = Column(String, nullable = False)

    sect = relationship("section", back_populates = "cours")

class section(Base):
    __tablename__ = "section"
    id_section = Column(UUID(as_uuid= True), primary_key = True, default = uuid.uuid4)
    id_cours = Column(UUID(as_uuid = True), ForeignKey("course.id_course", ondelete = "CASCADE"), nullable= False)

    cours = relationship("course", back_populates = "sect")
    chap = relationship("chapter", back_populates = "sectn")

class chapter(Base):
    __tablename__ = "chapter"
    id_chapter = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    num_caps = Column(String(30), nullable = False)
    duration = Column(String, nullable = False)
    numero = Column(Integer, nullable = True)
    id_sect = Column(UUID(as_uuid = True), ForeignKey("section.id_section", ondelete = "CASCADE"), nullable = False)
    complete = Column(Boolean, default = 0)
    url_image = Column(String)

    sectn = relationship("section", back_populates = "chap")
    cont = relationship("content", back_populates = "chpt")

class content(Base):
    __tablename__ = "content"
    id_content = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    content = Column(String, nullable = False)
    url_video = Column(Text, nullable = True)
    complete = Column(Boolean, default = 0)
    id_chap = Column(UUID(as_uuid = True), ForeignKey("chapter.id_chapter", ondelete = "CASCADE"), nullable = False)

    chpt = relationship("chapter", back_populates = "cont")

