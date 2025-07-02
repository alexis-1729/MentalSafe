from fastapi import FastAPI
from .database import get_db, Base, engine
from .routes import router

#Creando tablas de la db
Base.metadata.create_all(bind = engine)
#Inicia fastapi
app = FastAPI()
#incluye los endpoints o los registra
app.include_router(router)


