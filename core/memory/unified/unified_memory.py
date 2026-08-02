from core.memory.unified.memory_bridge import memory_bridge
from core.memory.unified.memory_router import memory_router


class UnifiedMemoryCore:


    def store(self, data):

        return memory_bridge.save(data)


    def recall(self):

        return {
            "memory": memory_bridge.recall(),
            "status": "UNIFIED_MEMORY_RECALL_ACTIVE"
        }


    def status(self):

        return {
            "router": "active",
            "bridge": "active",
            "status": "UNIFIED_MEMORY_CORE_ACTIVE"
        }



unified_memory = UnifiedMemoryCore()
