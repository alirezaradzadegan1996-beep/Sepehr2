

class LongTermMemory:

    def store(self,data):
        return {
            "memory":data,
            "storage":"completed",
            "status":"LONG_TERM_MEMORY_ACTIVE"
        }


long_term_memory=LongTermMemory()

