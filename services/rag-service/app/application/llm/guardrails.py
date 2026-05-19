import re

class GuardraiException(Exception):
    pass

class Guardrails:

    CODE_PATTERNS =[
        r"#include\s*<",
        r"int\s+main\s*\(",
        r"def\s+w+\(",
        r"class\s+\w+",
    ]

    FORBIDDEN_KEYWOARDS = [
        "solucion completa",
        "codigo completo",
        "resuelvelo",
        "respuesta final"
    ]

    def validate_request(self, user_text: str):
        for word in self.FORBIDDEN_KEYWOARDS:
            if word in user_text.lower():
                raise GuardraiException("Forbidden request detected")
    
    def santize_response(self, text: str)-> str:
        for pattern in self.CODE_PATTERNS:
            text = re.sub(pattern, "[code omitted]", text)
        print(text)
        return text
