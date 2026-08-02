
class AgentRegistry:

    def __init__(self):

        self.agents = {}


    def register(self, name, agent):

        self.agents[name] = agent

        return {
            "agent": name,
            "status": "registered"
        }


    def all(self):

        return list(
            self.agents.keys()
        )


agent_registry = AgentRegistry()
