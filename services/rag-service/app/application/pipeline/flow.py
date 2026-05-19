from app.application.services.llmService import llmService
from app.application.services.nlpService import nlpService
from app.infraestructure.embeddings.chunking import ChunkService
from app.infraestructure.embeddings.build_embedding import EmbeddingService
from app.infraestructure.embeddings.retrival import Retrieval
from app.application.llm.orchestrator import Orchestrator
from app.application.schema import InputOrchestator
class Pipeline:

    def __init__(self, 
                name: str):
            self.name = name

    async def pipeline(self, text)-> str:
        nlp = nlpService(text)
        sentiment = await nlp.get_sentiment()
        search = self.query(text)
        input = InputOrchestator(
              message= text,
              sentiment = sentiment,
              search= search
        )
        prompt = Orchestrator().run(input)
        llm = llmService(prompt).get_response()
        return llm



    def build_embeddings(self, text:str):
    
            #obtenemos chunks
            self.chunk = ChunkService(text)
            chunks = self.chunk.divide()

            self.embedding = EmbeddingService(self.name)
            self.embedding.create_collection()
            #obtenemos embeddings
            embeddings = self.embedding.build(chunks)
            return embeddings
    

    def query(self, query:str):
            self.retrieval = Retrieval(self.name)

            result = self.retrieval.search(query)

            return result



