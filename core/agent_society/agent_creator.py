

class AgentCreator:

    def create(self,name,skill):
        return {
            "agent":name,
            "skill":skill,
            "status":"AGENT_CREATION_ACTIVE"
        }


agent_creator=AgentCreator()

