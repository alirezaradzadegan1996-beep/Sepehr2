
from core.memory.session_memory import session_memory
from core.memory.memory_retriever import memory_retriever


class MemoryRuntimeBridge:

    def remember(self,message):
        return session_memory.save({
            "message":message
        })


    def recall(self,query):
        return memory_retriever.search(query)


memory_runtime_bridge=MemoryRuntimeBridge()
