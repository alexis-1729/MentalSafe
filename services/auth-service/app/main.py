from fastapi import FastAPI
from app.infrastructure.db.database import Base, engine
from app.api.routers import router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(router)

