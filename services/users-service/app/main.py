from fastapi import FastAPI
from app.api.routers import api_router
from app.infrastructure.db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Users Microservice")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Users Service is online"}