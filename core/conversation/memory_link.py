
class MemoryLink:

    def save(self,data):
        return {
            "memory":data,
            "status":"saved"
        }

memory_link = MemoryLink()
