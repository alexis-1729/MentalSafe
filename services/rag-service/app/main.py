from fastapi import FastAPI
from app.api.routers import router
from app.infraestructure.database import Base, engine

app = FastAPI(
    title="RAG Service API",
    description="API para servicio de RAG (Retrieval-Augmented Generation)",
    version="1.0.0"
)

@app.on_Event("statrup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Incluir routers
app.include_router(router)

