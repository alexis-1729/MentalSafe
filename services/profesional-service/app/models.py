from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class profesionalData(Base):
    __tablename__ = "profesional"
    id = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name = Column(String(40), nullable = False)
    apellido_pa = Column(String(40), nullable= False)
    apellido_ma= Column(String(40), nullable = False)
    email = Column(String(50), nullable = False)
    country = Column(String(50), nullable = False)
    city = Column(String(50), nullable = False)
    id_profesional = Column(UUID(as_uuid = True), nullable = False, unique = True) #pk del microservicio externo
    certification = Column(String, default = "No")
    activate= Column(Boolean, default = 0)

    speciallity = relationship("profesionalScpeciallity", back_populates = "profesional")
    workExp = relationship("workExperience", back_populates = "proData")
    star = relationship("stars", back_populates = "pro")

class profesionalScpeciallity(Base):
    __tablename__ = "speciallity"
    id_proEsp = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    id_pro = Column(UUID(as_uuid = True), ForeignKey("profesional.id_profesional", ondelete = "CASCADE"), nullable = False)
    id_speciallity = Column(UUID(as_uuid = True),ForeignKey("speciallityData.id_speciallity", ondelete = "CASCADE") ,nullable = False)

    profesional = relationship("profesionalData", back_populates = "speciallity")
    espName = relationship("speciallityData", back_populates = "proEsp")

class speciallityData(Base):
    __tablename__ = "speciallityData"
    id_speciallity = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name = Column(String(40), nullable = False)
    description =Column(Text, nullable = False)

    proEsp = relationship("profesionalScpeciallity", back_populates = "espName")

class workExperience(Base):
    __tablename__ = "workExperience"
    id_exp = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    id_pro = Column(UUID(as_uuid = True), ForeignKey("profesional.id_profesional", ondelete = "CASCADE"), nullable = False)
    id_experience_data = Column(UUID(as_uuid = True), ForeignKey("experienceData.id_data", ondelete = "CASCADE") ,nullable = False)

    expData = relationship("experienceData", back_populates = "work")
    proData = relationship("profesionalData", back_populates = "workExp")

class experienceData(Base):
    __tablename__ = "experienceData"
    id_data = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    companyInst = Column(String(50), nullable = False)
    position = Column(String(50), nullable = False)
    sector = Column(String(50), nullable = False)
    description = Column(String(50), nullable = False)
    start_date = Column(DateTime(timezone = True))
    finish_date = Column(DateTime(timezone = True))

    work = relationship("workExperience", back_populates = "expData")

class stars(Base):
    __tablename__ = "starsProfesional"
    id_star = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    id_prof = Column(UUID(as_uuid = True), ForeignKey("profesional.id_profesional", ondelete = "CASCADE"), nullable = False)
    five = Column(Integer, default = 0)
    four = Column(Integer, default = 0)
    three = Column(Integer, default = 0)
    two = Column(Integer, default = 0)
    one = Column(Integer, default = 0)
    media = Column(Float, default = 0.0)

    pro = relationship("profesionalData", back_populates = "star")




