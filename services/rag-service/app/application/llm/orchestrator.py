from app.application.llm.context_builder import ContextBuilder
from app.application.llm.prompt_loader import PromptLoader
from app.application.llm.guardrails import Guardrails 
from app.application.schema import InputOrchestator

class Orchestrator:
    def __init__(self):
        self.context_builder = ContextBuilder()
        self.promptLoader = PromptLoader()
        self.guardrails = Guardrails()

    def run(self, request: InputOrchestator)-> str:
        self._validate_request(request)

        # self.guardrails.vali date_request(request.context)
        
        context_prompt = self.context_builder.build(request)


        prompt = self._build_prompts(context_prompt)


        #safe_response = self.guardrails.santize_response(raw_response)

        return prompt
    
    def _validate_request(self, request: InputOrchestator):
        if request.sentiment is None:
            return ValueError("Action requerida")
        
    def _build_prompts(self, context_prompt: str):
        system_prompt = self.promptLoader.load("system")

        prompt = (
            f"System Prompt:\n{system_prompt}"
            f"{context_prompt}\n\n"   
        )
        return prompt

        