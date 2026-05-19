from fastapi import APIRouter, HTTPException, Request
from ..schemas.inputSchema import Input, Output
from ...componentes.post_processor import PostProcessor

router = APIRouter()
refiner = PostProcessor()


@router.post("/predict")

def prediction(request: Request, text: Input):
    try:
        transformer = request.app.state.transformer
        predictor = request.app.state.predictor
        features = transformer.preprocess(text.text)

        prediction_raw = predictor.predict(features)

        result = refiner.format(prediction_raw)

       

        return result
    except ValueError as ve:
        raise HTTPException(status_code = 404, detail = str(ve))
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))
