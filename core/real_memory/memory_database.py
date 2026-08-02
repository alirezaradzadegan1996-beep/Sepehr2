

class MemoryDatabase:

    def save(self,data):
        return {
            "data":data,
            "saved":True,
            "status":"MEMORY_DATABASE_ACTIVE"
        }

memory_database=MemoryDatabase()

