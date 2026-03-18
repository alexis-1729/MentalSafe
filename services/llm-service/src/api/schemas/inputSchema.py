from pydantic import BaseModel

class Input(BaseModel):
    user: str
    system: str

class Output(BaseModel):
    response: str