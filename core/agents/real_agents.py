

class Agent:

    def __init__(self,name):
        self.name=name


    def run(self,task):
        return {
            "agent":self.name,
            "task":task,
            "status":"AGENT_EXECUTION_ACTIVE"
        }


research_agent=Agent("research_agent")
coding_agent=Agent("coding_agent")
planning_agent=Agent("planning_agent")

