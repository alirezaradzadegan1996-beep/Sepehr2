
class SelfAwarenessMemory:

    def save(self,data):
        return {
            "memory":data,
            "status":"saved"
        }


self_awareness_memory = SelfAwarenessMemory()
