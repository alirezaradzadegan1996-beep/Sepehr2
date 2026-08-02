
class MemoryMount:
    def mount(self):
        return {
            "memory":"mounted",
            "status":"MEMORY_SYSTEM_MOUNT_ACTIVE"
        }

memory_mount=MemoryMount()
