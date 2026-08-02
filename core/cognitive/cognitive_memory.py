from core.memory.unified.unified_memory import unified_memory


class CognitiveMemory:


    def remember(self, data):

        return unified_memory.store(data)


    def recall(self):

        return unified_memory.recall()


    def analyze(self):

        memory = self.recall()

        return {
            "memory_available": True,
            "items": memory["memory"]["count"],
            "status": "COGNITIVE_MEMORY_ANALYSIS_ACTIVE"
        }


    def status(self):

        return {
            "gateway": "active",
            "reasoning_link": "active",
            "context_link": "active",
            "status": "COGNITIVE_MEMORY_CORE_ACTIVE"
        }



cognitive_memory = CognitiveMemory()
