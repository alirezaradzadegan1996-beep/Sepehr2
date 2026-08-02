
from core.llm.llm_router import llm_router


class ReasoningBridge:

    def think(self, problem):

        result = llm_router.route(
            problem
        )

        return {
            "problem": problem,
            "reasoning": result,
            "status": "completed"
        }


reasoning_bridge = ReasoningBridge()
