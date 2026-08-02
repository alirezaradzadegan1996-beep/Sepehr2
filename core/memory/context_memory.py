
class ContextMemory:

    def update(self,context):
        return {
            "context":context,
            "status":"updated"
        }


context_memory=ContextMemory()
