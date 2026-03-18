from fastapi import FastAPI
from app.routes import ia_messages, ia_sessions, ia_chat
from app.database import Base, engine

from app.models import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ia_chat.router)
app.include_router(ia_messages.router)
app.include_router(ia_sessions.router)

 


