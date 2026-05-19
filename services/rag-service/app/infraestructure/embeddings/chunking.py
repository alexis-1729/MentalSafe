class ChunkService:

    def __init__(self,text:str, minSize:int = 50, maxSize:int=124, ender: str='.'): 
            self.minSize = minSize
            self.maxSize = maxSize
            self.text = text
            self.ender = ender

    def divide(self):

        chunks = []  
        aux: str = ""
        for letra in self.text:
            if len(aux) + 1 >= self.minSize and len(aux) + 1 <= self.maxSize and letra == self.ender:
                aux += letra
            else:
                chunks.append(aux)
                aux = ""

        if aux:
            chunks.append(aux)

        return chunks
    
