from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.llmRoute import router as llm_router
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(
    title="LLM Service",
    description="Servicio de LLM con Gemini",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(llm_router, prefix="/api/v1/llm", tags=["LLM"])


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}
