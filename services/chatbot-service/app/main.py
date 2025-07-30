from fastapi import FastAPI
from app.routes import ia_messages, ia_sessions, ia_chat
from .database import Base, engine
#Inicializar clave de API de Google
#Crear las tablas
Base.metadata.create_all(bind=engine)

#Inicializar 
app = FastAPI()

app.include_router(ia_chat.router)
app.include_router(ia_messages.router)
app.include_router(ia_sessions.router)

 


