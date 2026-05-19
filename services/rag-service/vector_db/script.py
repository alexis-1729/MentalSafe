from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer


# 1. Configurar el cliente (usa 'localhost' si el script corre en la misma EC2)

client = QdrantClient(host="localhost", port=6333)

# 2. Cargar el modelo de embeddings (ligero y rápido)
model = SentenceTransformer('all-MiniLM-L6-v2') 
# Este modelo genera vectores de 384 dimensiones

COLLECTION_NAME = "Mental"

# 3. Crear la colección (solo se hace una vez)
client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

# 4. Supongamos que aquí tienes tus 1,000 chunks
minSize = 50
maxSize = 128
ender = '.'
ender2= ','

with open('/home/alexis-1729/Documentos/Tratamiento de la Depresión.txt', 'r', encoding = 'utf-8') as file:
     text = file.read()

chunks = []  
aux: str = ""
for letra in text:
        if len(aux) + 1 >= minSize and len(aux) + 1 <= maxSize and (letra == ender or letra == ender2):
            aux += letra
        else:
            chunks.append(aux)
            aux = ""

if aux:
    chunks.append(aux)

# 5. Generar embeddings y subirlos
points = []
for i, text in enumerate(chunks):
    vector = model.encode(text).tolist()
    points.append(PointStruct(
        id=i, 
        vector=vector, 
        payload={"text": text}  # Guardamos el texto original junto al vector
    ))

BATCH_SIZE = 64

for i in range(0, len(points), BATCH_SIZE):
    batch = points[i:i+BATCH_SIZE]
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=batch
    )

print(f"¡Éxito! {len(chunks)} vectores subidos a Qdrant.")