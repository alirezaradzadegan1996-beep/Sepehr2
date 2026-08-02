
class MemoryEncoder:

    def encode(self,message):
        return {
            "memory":"encoded",
            "status":"CONVERSATION_MEMORY_ENCODER_ACTIVE"
        }

memory_encoder=MemoryEncoder()
