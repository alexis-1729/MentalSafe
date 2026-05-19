from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

class EmbeddingService:

    def __init__(self, name):
        self.client = QdrantClient(host = "localhost", port = 6333)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.name = name

    def create_collection(self):
        self.client.recreate_collection(
            collection_name = self.name,
            vectors_config = VectorParams(size=384, distance= Distance.COSINE),
        )
    
    def build(self, chunks):
        points = []

        for i, text in enumerate(chunks):
            vector = self.model.encode(text).tolist()
            points.append(PointStruct(
                id= i,
                vector = vector,
                payload={ "text": text}    
            ))
        self.client.upsert(collection_name = self.name, points= points)