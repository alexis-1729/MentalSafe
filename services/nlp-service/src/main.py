from fastapi import FastAPI
from contextlib import asynccontextmanager
from .componentes.pre_processor import PreProcessor
from .componentes.predictor import ModelPredictor
from .api.routers import api_v1_router
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger("ggpapa")

transformer = PreProcessor()
predictor = ModelPredictor()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Iniciando microservice ML")

    try:
        predictor.load_model()
        transformer.load_scaler()

        app.state.predictor = predictor
        app.state.transformer = transformer
        logger.info("Modelo y Scales cargados")
    except Exception as e:
        logger.error(f"Error en el inicio: {e}")
        raise RuntimeError("No se pudo iniciar")
    yield

    logger.info("Valio cola el microservicio")

app = FastAPI(title = "ML microservice", lifespan = lifespan)

app.include_router(api_v1_router)