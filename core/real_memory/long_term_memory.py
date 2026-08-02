
class LongTermMemory:

    def activate(self):
        return {
            "memory":"persistent",
            "status":"LONG_TERM_MEMORY_CORE_ACTIVE"
        }

long_term_memory=LongTermMemory()
