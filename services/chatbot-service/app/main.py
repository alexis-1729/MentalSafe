from fastapi import FastAPI
from app.routes import ia_messages, ia_sessions
import google.generativeai as genai
import dotenv
from .database import Base, engine
import os
#

#Cargar variables de entorno
load_dotenv()

#Inicializar clave de API de Google
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Crear las tablas
Base.metadata.create_all(bind=engine)

#Inicializar 
app = FastAPI()



#
app.include_router(ia_messages.router)
app.include_router(ia_sessions.router)

 


