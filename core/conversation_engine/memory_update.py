

class ConversationMemory:

    def update(self):
        return {
            "memory":"updated",
            "status":"CONVERSATION_MEMORY_UPDATE_ACTIVE"
        }


conversation_memory=ConversationMemory()

