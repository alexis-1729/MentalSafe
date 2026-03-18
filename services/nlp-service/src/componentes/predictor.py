from transformers import BertTokenizer, BertForSequenceClassfication
import torch

class ModelPredictor:

    def __init__(self):
        self.model = None

    def load_model(self):
        model_path = "secret on config"

        self.model = BertForSequenceClassfication(model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def predict(self, inputs):

        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**input)

        
        return outputs
