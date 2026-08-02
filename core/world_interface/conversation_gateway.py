

class ConversationGateway:

    def connect(self):
        return {
            "conversation":"ready",
            "status":"HUMAN_CONVERSATION_GATEWAY_ACTIVE"
        }


conversation_gateway=ConversationGateway()

