from fastapi import APIRouter, HTTPException
from src.api.schemas.inputSchema import Input, Output
from src.componentes.post_processor import PostProcessor
from src.componentes.pre_processor import PreProcessor
from src.componentes.predictor import ModelPredictor

router = APIRouter()
refiner = PostProcessor()
transformer = PreProcessor()
predictor = ModelPredictor()

@router.post("predict")

def prediction(text: Input):
    try:
        features = transformer.preprocess(text)

        prediction_raw = predictor.predict(features)

        result = refiner.format(prediction_raw)

        ans = Output(
            sentiment = result
        )

        return ans
    except ValueError as ve:
        raise HTTPException(status_code = 404, detail = str(ve))
    
    except Exception as e:
        raise HTTPException(status_code = 500,detail = "Internal error")
