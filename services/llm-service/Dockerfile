# etapa 1: Builder- dependencias

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recomends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

#etapa 2: runtime

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local

RUN useradd -m mluser
USER mluser

COPY --chown=mluser:mluser src/ ./src/
COPY --chown=mluser:mluser models/ ./models/

ENV MODEL_PATH=/app/models/model_v1.onnx
ENV PYTHONPATH=/app/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8003", "--workers", "1"]
