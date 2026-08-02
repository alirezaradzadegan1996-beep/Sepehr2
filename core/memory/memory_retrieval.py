
from core.memory.long_term_memory import long_term_memory


class MemoryRetrieval:

    def search(self, query):

        memories = long_term_memory.all()

        return {
            "query": query,
            "results": memories,
            "status": "retrieved"
        }


memory_retrieval = MemoryRetrieval()
