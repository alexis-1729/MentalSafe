from fastapi import FastAPI
from app.api.routers import api_router
from app.infrastructure.database import engine, Base

app = FastAPI(title="Users Microservice")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Users Service is online"}