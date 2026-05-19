from fastapi import APIRouter, HTTPException
import google.generativeai as genai
import os
from .schemas import PromptRequest, PromptResponse

router = APIRouter()

# Configurar la API key de Google
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)


@router.post("/gemma", response_model=PromptResponse)
async def generate_with_gemma(request: PromptRequest):
    """
    Endpoint para enviar un prompt a la API de Gemini (anteriormente Gemma)
    
    Args:
        request: PromptRequest con el prompt y configuración
        
    Returns:
        PromptResponse con la respuesta del modelo
    """
    try:
        if not GOOGLE_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="GOOGLE_API_KEY no está configurada"
            )
        
        # Usar el modelo Gemini (Gemma)
        model = genai.GenerativeModel('gemma-4-31b-it')
        
        # Generar contenido
        response = model.generate_content(
            request.prompt,
            generation_config=genai.GenerationConfig(
                max_output_tokens=request.max_tokens,
                temperature=request.temperature,
            )
        )
        
        return PromptResponse(
            response=response.text,
            model="gemma-3-27b-it"
        )
        
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error en el formato del prompt: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar la solicitud: {str(e)}"
        )
