from pydantic import BaseModel, UUID4
from uuid import UUID

class RecomendationResponse(BaseModel):
    id_test: UUID4
    name: str
    