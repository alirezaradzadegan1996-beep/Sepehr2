from core.cognitive.self_reasoning import self_reasoning
from core.cognitive.problem_understanding import problem_understanding
from core.cognitive.solution_generator import solution_generator
from core.cognitive.knowledge_bridge import knowledge_bridge


class ReasoningBridge:

    def think(self, problem):

        knowledge = knowledge_bridge.query(problem)

        understood = problem_understanding.understand(
            problem
        )

        analysis = self_reasoning.analyze(
            {
                **understood,
                "knowledge": knowledge,
                "has_knowledge": knowledge.get("status") == "found"
            }
        )

        solution = solution_generator.generate(
            analysis
        )

        return {
            "understanding": understood,
            "knowledge": knowledge,
            "analysis": analysis,
            "solution": solution,
            "status": "thinking_completed"
        }


reasoning_bridge = ReasoningBridge()
