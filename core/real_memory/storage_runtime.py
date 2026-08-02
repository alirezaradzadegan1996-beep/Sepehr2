
class StorageRuntime:

    def save(self,data):
        return {
            "storage":"saved",
            "status":"MEMORY_STORAGE_RUNTIME_ACTIVE"
        }

storage_runtime=StorageRuntime()
