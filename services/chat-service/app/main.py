from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import dialogflow_v2 as dialogflow
import os

app = FastAPI()

# Carga de variables de entorno
PROJECT_ID = os.getenv("DIALOGFLOW_PROJECT_ID")

class MessageRequest(BaseModel):
    session_id: str
    message: str
    language_code: str = "es"  

@app.post("/dialogflow/message")
def send_message(request: MessageRequest):
    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(PROJECT_ID, request.session_id)

        text_input = dialogflow.TextInput(text=request.message, language_code=request.language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(session=session, query_input=query_input)

        return {
            "response": response.query_result.fulfillment_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
