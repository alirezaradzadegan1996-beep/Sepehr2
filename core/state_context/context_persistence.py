

class ContextPersistence:

    def save(self,context):
        return {
            "context":context,
            "storage":"persistent",
            "status":"CONTEXT_PERSISTENCE_ACTIVE"
        }


context_persistence=ContextPersistence()

