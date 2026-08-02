
from core.agents.agent_registry import agent_registry
from core.agents.specialized_agents import (
    research_agent,
    coding_agent,
    evaluation_agent
)


class AgentOrchestrator:

    def start(self, task):

        agent_registry.register(
            "research",
            research_agent
        )

        agent_registry.register(
            "coding",
            coding_agent
        )

        agent_registry.register(
            "evaluation",
            evaluation_agent
        )


        return {
            "research":
                research_agent.run(task),

            "coding":
                coding_agent.run(task),

            "evaluation":
                evaluation_agent.run(task),

            "status":
                "MULTI_AGENT_ACTIVE"
        }


agent_orchestrator = AgentOrchestrator()
