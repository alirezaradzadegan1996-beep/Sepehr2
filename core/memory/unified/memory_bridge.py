from core.memory.experience_memory import experience_memory


class MemoryBridge:


    def save(self, data):

        return experience_memory.save(data)


    def recall(self):

        return experience_memory.recall()



memory_bridge = MemoryBridge()
