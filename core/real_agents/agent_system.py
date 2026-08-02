

class Agent:

    def __init__(self,name,role):
        self.name=name
        self.role=role


    def execute(self,task):

        return {

            "agent":self.name,
            "role":self.role,
            "task":task,
            "status":"AGENT_TASK_EXECUTION_ACTIVE"

        }



class AgentRegistry:

    def __init__(self):
        self.agents=[]


    def register(self,agent):
        self.agents.append(agent)

        return {

            "agent":agent.name,
            "status":"AGENT_REGISTERED"

        }



registry=AgentRegistry()

reasoning_agent=Agent(
"reasoning_agent",
"reasoning"
)

coding_agent=Agent(
"coding_agent",
"coding"
)

planning_agent=Agent(
"planning_agent",
"planning"
)

