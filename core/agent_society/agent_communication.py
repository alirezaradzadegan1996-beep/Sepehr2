

class AgentCommunication:

    def send(self,message):
        return {
            "message":message,
            "communication":"active",
            "status":"AGENT_COMMUNICATION_ACTIVE"
        }


agent_communication=AgentCommunication()

