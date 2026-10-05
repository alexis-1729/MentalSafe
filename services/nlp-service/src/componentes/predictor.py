from transformers import  BertForSequenceClassification
import torch
from pathlib import Path
import logging
class ModelPredictor:

    def __init__(self):
        self.model = None
        self.logger = logging.getLogger("predictor")

    def load_model(self):
        base = Path(__file__).resolve().parent.parent.parent
        model_path =base / "models"

        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def predict(self, inputs):
        try:
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            with torch.no_grad():
                outputs = self.model(**inputs)

            
            return outputs
        except Exception as e:
            self.logger.error(f"Error: {e}")
