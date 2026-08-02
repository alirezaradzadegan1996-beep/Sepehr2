
class MemoryRetriever:

    def search(self,query):
        return {
            "query":query,
            "memory":"found",
            "status":"retrieved"
        }


memory_retriever=MemoryRetriever()
