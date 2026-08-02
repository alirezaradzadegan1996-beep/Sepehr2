
from core.cognitive.self_reasoning import self_reasoning
from core.cognitive.problem_understanding import problem_understanding
from core.cognitive.solution_generator import solution_generator


class ReasoningBridge:

    def think(self, problem):

        understood = problem_understanding.understand(problem)

        analysis = self_reasoning.analyze(
            understood
        )

        solution = solution_generator.generate(
            analysis
        )

        return {
            "understanding": understood,
            "analysis": analysis,
            "solution": solution,
            "status":"thinking_completed"
        }


reasoning_bridge = ReasoningBridge()
