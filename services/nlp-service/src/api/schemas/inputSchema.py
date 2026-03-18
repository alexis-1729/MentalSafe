from pydantic import BaseModel

class Input(BaseModel):
    text : str

class Output(BaseModel):
    sentiment: str