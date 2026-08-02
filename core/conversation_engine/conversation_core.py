

class ConversationCore:

    def activate(self):
        return {
            "input":"active",
            "understanding":"active",
            "response":"active",
            "status":"REAL_CONVERSATION_CORE_ACTIVE"
        }


conversation_core=ConversationCore()

