from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

# Inicializar clave de API de Google
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Crear las tablas si no existen
models.Base.metadata.create_all(bind=engine)

# Inicializar la app FastAPI
app = FastAPI()

# Esquema de entrada
class ChatMessage(BaseModel):
    message: str
    session_id: str = None

# Endpoint de conversación
@app.post("/chat")
def chat_with_gemini(chat: ChatMessage):
    try:
        # Inicializar cliente Gemini
        model = genai.GenerativeModel("gemma-3-12b-it")
        response = model.generate_content(chat.message)
        reply = response.text

        # Guardar historial en base de datos
        db: Session = SessionLocal()
        new_entry = models.ChatHistory(
            session_id=chat.session_id or "default",
            user_message=chat.message,
            bot_reply=reply
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        db.close()
#retorno de idsesion
        return {"reply": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para obtener historial de una sesión
@app.get("/history/{session_id}")
def get_history(session_id: str):
    try:
        db: Session = SessionLocal()
        history = db.query(models.ChatHistory).filter_by(session_id=session_id).all()
        db.close()

        return [{"user": h.user_message, "bot": h.bot_reply} for h in history]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
