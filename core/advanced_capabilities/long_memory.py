

class LongMemory:

    def store(self,data):
        return {
            "memory":data,
            "learning":"updated",
            "status":"LONG_TERM_MEMORY_ACTIVE"
        }

long_memory=LongMemory()

