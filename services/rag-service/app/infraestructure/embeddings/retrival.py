from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

class Retrieval:

    def __init__(self, name):
        self.client = QdrantClient(host = "localhost", port = 6333)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.name = name

    def search(self, text):
        query_vector = self.model.encode(text).tolist()
        search_result = self.client.search(
            collection_name = self.name,
            query_vector=query_vector,
            limit = 3
        )

        return search_result