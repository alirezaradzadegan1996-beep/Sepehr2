

class AgentManager:

    def create(self,name):
        return {
            "agent":name,
            "status":"AGENT_CREATED_ACTIVE"
        }


    def manage(self):
        return {
            "agents":"managed",
            "status":"AGENT_MANAGER_ACTIVE"
        }


agent_manager=AgentManager()

