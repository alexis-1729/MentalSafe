from fastapi import FastAPI
from app.api.routers import router
from app.infraestructure.database import Base, engine


app = FastAPI()

@app.on_Event("statrup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(router)
