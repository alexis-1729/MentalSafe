from fastapi import FastAPI
from app.api.v1.test_router import router as test_user_router

app = FastAPI(
    title="Test Service - Clean Architecture",
    description="Microservicio para la gestión de tests y resultados",
    version="1.0.0"
)

# Registro de rutas
app.include_router(test_user_router, prefix="/api/v1/tests", tags=["Tests"])

@app.get("/")
def read_root():
    return {"message": "Test Service is running"}