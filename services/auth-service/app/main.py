from fastapi import FastAPI
from app.db import get_connection

app = FastAPI()

@app.get("/")
def root():
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        conn.close()
        return {"message": "Conexión exitosa", "hora_actual": result}
    else:
        return {"message": "No se pudo conectar a la base de datos"}
