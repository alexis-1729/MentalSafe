
import torch
import logging
class PostProcessor:

    def __init__(self) -> None:
        self.labels = {
            0: "enojo",
            1: "miedo",
            2: "alegria",
            3: "amor",
            4: "tristeza",
            5: "sorpresa"
        }
        self.logger = logging.getLogger("post")

    def format(self, outputs):
        try:
            logits = outputs.logits
            prediction =torch.argmax(logits, dim = 1).item()

            return self.labels[prediction]
        except Exception as e:
            self.logger.error(f"Error: {e}")