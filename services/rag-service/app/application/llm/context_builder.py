from app.application.schema import InputOrchestator


class ContextBuilder:

    def build(self, input: InputOrchestator) -> str:
        
        # Construir la sección de contexto de búsqueda
        context_section = ""
        if input.search:
            context_section = "Contexto relevante encontrado:\n"
            for idx, item in enumerate(input.search, 1):
                context_section += f"{idx}. (Score: {item.score:.2f}) {item.pyload}\n"
        
        # Construir el prompt final
        prompt = f"""
        Información del usuario:
        - Mensaje: {input.message}
        - Sentimiento detectado: {input.sentiment}

        {context_section}

        Basado en la información anterior, proporciona una respuesta empática, útil y contextualizada."""
                
        return prompt