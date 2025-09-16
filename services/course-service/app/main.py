from fastapi import FastAPI
from .database import  Base, engine
from app.routes import course


Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(course.router)

 