from fastapi import HTTPException
from pydantic import UUID4
from app import models
from app.schemas.chat import *
from sqlalchemy.orm import Session
from app.models import ChatSessions, ChatMessage
from datetime import datetime
import uuid
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def create_new_message(session_id: UUID4, payload: ChatMessageCreate,
    db: Session):

     #Crear el mensaje
    new_message = ChatMessage(
        session_id = session_id,
        sender = payload.sender,
        message = payload.content,
        emotion_tag= "gg" 
    )

#Guardamos mensaje de usuario
    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    try:
        #conecction with IA
        model = genai.GenerativeModel("gemma-3-27b-it")
        response = model.generate_content(payload.content)
        reply = response.text

        new= ChatMessage(
            session_id= session_id,
            sender = "ia",
            message=reply,
            emotion_tag= "gg" 
)
        #guardamos mensaje de ia
        db.add(new)
        db.commit()
        db.refresh(new)

        return reply
    except Exception: 
        return HTTPException(status_code= 404, detail= "Failes conecction")
