from pydantic import BaseModel
from typing import Union, List

class Item(BaseModel):
    id: Union[int, str]
    score: float
    pyload: str

class InputOrchestator(BaseModel):
    message: str
    sentiment: str
    search: List[Item]