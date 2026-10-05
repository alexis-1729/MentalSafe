from fastapi import FastAPI
from .database import Base, engine
from app.routes import profesional, speciallity, workExperience 


Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(profesional.router)
app.include_router(workExperience.router)
app.include_router(speciallity.router)