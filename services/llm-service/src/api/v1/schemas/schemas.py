from pydantic import BaseModel, Field


class PromptRequest(BaseModel):
    """Schema para las solicitudes de prompt"""
    prompt: str = Field(..., min_length=1, description="El prompt a enviar al modelo")
    max_tokens: int = Field(default=1000, ge=1, le=4096, description="Máximo de tokens en la respuesta")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="Temperatura de generación (0-2)")


class PromptResponse(BaseModel):
    """Schema para las respuestas del LLM"""
    response: str = Field(..., description="Respuesta generada por el modelo")
    model: str = Field(default="gemini-2.0-flash", description="Modelo utilizado")
