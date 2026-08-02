

class CommunicationBus:

    def connect(self):
        return {
            "communication":"active",
            "status":"AGENT_COMMUNICATION_BUS_ACTIVE"
        }


communication_bus=CommunicationBus()

