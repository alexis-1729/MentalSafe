from fastapi import HTTPException
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class nlpService:

    def __init__(self, text):
        self.path = os.getenv("NLP_PATH")
        if not self.path:
            raise ValueError("NLP_PATH environment variable is not set")
        self.text = text

    async def get_sentiment(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.path, # type: ignore
                    json={"text": self.text})
                if response.status_code == 404:
                    raise HTTPException(status_code= 404, detail= "Failed")
                elif response.status_code != 200:
                    raise HTTPException(status_code= 500, detail = "error server")
                return response.text
        except httpx.RequestError as e:
            raise HTTPException(status_code= 503, detail = f"Conection failed: {str(e)}")
    