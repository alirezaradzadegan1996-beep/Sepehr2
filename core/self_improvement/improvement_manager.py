from core.self_improvement.problem_detector import problem_detector
from core.self_improvement.solution_planner import solution_planner
from core.self_improvement.improvement_memory import improvement_memory


class SelfImprovementManager:

    def analyze(
        self,
        task,
        experience_analysis=None,
        memory_analysis=None,
        decision=None
    ):

        detection = problem_detector.analyze(
            task,
            experience_analysis,
            memory_analysis,
            decision
        )

        if detection["needs_improvement"]:

            plan = solution_planner.plan(
                detection
            )

            improvement_memory.save({
                "task":task,
                "problems":detection["problems"],
                "plan":plan["plans"],
                "status":"planned"
            })

            return {
                "status":"improvement_needed",
                "analysis":detection,
                "plan":plan
            }


        return {
            "status":"stable",
            "analysis":detection
        }


self_improvement_manager = SelfImprovementManager()
