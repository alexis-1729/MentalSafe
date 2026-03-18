from transformers import BertTokenizer
import re
class PreProcessor:

    def __init__(self):
        self.tokenizer = None

    def load_scaler(self):
        model_path = "secret"

        self.tokenizer = BertTokenizer(model_path)

    @staticmethod
    def clean_text(input: str):
        input  = re.sub(r"http\S+", "", input)
        input = re.sub(r"<.*?","", "input")
        input = re.sub(r"\s+", " ", input)
        return input.strip()

    def preprocess(self, input: str):

        inputs = self.clean_text(input)
        inputs = self.tokenizer(
            input, 
            return_tensors = "pt",
            truncation = True,
            padding = True,
            max_length = True,
            max_length = 128
        )

        return inputs