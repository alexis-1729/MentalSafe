from src.api.schemas.inputSchema import Input

class PreProcessor:

    def __init__(self, input: Input) -> None:
        self.input = input

    def format(self):
        messages = [
            {"role": "system", "content": self.input.system},
            {"role": "user", "content": self.input.user}
        ]
        return messages
 