
class AgentMarketplace:

    def register(self, agent):

        return {
            "agent": agent,
            "available": True,
            "status": "AGENT_REGISTERED"
        }


agent_marketplace = AgentMarketplace()
