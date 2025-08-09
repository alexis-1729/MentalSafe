import google.generativeai as genai
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def ask_ai(prompt):
    try:
        model = genai.GenerativeModel("gemma-3-27b-it")
        response = model.generate_content(prompt)
        reply = response.text
        return reply
    except:
        return HTTPException(status_code =  404, detail = "MAMO")

def interpret_score(test_name, score):
    prompt = f"""
Un usuario ha completado el test {test_name} y obtuvo un puntaje de {score}.
Devuelve una breve interpretación del resultado sin mencionar el puntaje, en un lenguaje claro y empático.
"""
    return ask_ai(prompt)