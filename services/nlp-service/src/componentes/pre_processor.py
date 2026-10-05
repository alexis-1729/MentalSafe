from transformers import AutoTokenizer
from dotenv import load_dotenv
from pathlib import Path
import logging
import re
import os

load_dotenv()

class PreProcessor:

    def __init__(self):
        self.tokenizer = None
        self.logger = logging.getLogger("preprocessor")

    def load_scaler(self):
        model_path = Path("/app/models")  # <- hardcode temporal

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

    @staticmethod
    def clean_text(input: str):
        input  = re.sub(r"http\S+", "", input)
        input = re.sub(r"<.*?","", "input")
        input = re.sub(r"\s+", " ", input)
        return input.strip()

    def preprocess(self, input: str):
        try:

            inputs = self.clean_text(input)
            inputs = self.tokenizer(
                inputs, 
                return_tensors = "pt",
                truncation = True,
                padding = True,
                max_length = 128
            )
            return inputs
        except Exception as e:
            self.logger.error(f"error: {e}")
