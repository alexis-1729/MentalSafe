from fastapi import HTTPException
from dotenv import load_dotenv
import logging
import httpx 
import os

load_dotenv()

class llmService:

    def __init__(self, prompt):
        self.path = os.getenv("LLM_PATH")
        self.prompt = prompt
        self.logger = logging.getLogger("llm")

    async def get_response(self)-> str:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                self.path,
                json= {"prompt": self.prompt})
                if response.status_code == 404:
                    raise HTTPException(status_code= 404, detail= "Failed")
                elif response.status_code != 200:
                    raise HTTPException(status_code= 500, detail = "error server")
                return response.text
        except httpx.RequestError as e:
            self.logger.error(f"Error: {e}")
            return "falla"
