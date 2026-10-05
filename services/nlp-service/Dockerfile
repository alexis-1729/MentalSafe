# Usamos una imagen base ligera de Python
FROM python:3.11-slim

# Variables de entorno para forzar CPU y evitar warnings
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias del sistema necesarias para compilar algunos paquetes
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiamos requirements e instalamos
COPY requirements.txt .
# Usamos el índice de CPU de PyTorch para reducir el tamaño de la imagen (~200MB menos)
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Copiamos el código de la aplicación
COPY src/ ./app/

# Copiamos los archivos del modelo 
COPY models/ ./models/

# Exponemos el puerto

# Comando de inicio con 1 worker (importante en CPU para no saturar RAM)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8008", "--workers", "1"]