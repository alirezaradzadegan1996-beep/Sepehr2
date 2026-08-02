

class MemoryStorage:

    def save(self,data):
        return {
            "data":data,
            "stored":True,
            "status":"MEMORY_STORAGE_ENGINE_ACTIVE"
        }


memory_storage=MemoryStorage()

