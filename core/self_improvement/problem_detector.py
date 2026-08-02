class ProblemDetector:

    def analyze(
        self,
        task,
        experience_analysis=None,
        memory_analysis=None,
        decision=None
    ):

        problems = []

        if experience_analysis:
            if experience_analysis.get("confidence",1) < 0.5:
                problems.append({
                    "type":"low_confidence",
                    "source":"experience"
                })

            if experience_analysis.get("successful_count",1) == 0:
                problems.append({
                    "type":"no_success_history",
                    "source":"experience"
                })

        if memory_analysis:
            if memory_analysis.get("learning_needed"):
                problems.append({
                    "type":"learning_needed",
                    "source":"memory"
                })

        if decision:
            if decision.get("decision") in [
                "cognitive_reasoning"
            ]:
                problems.append({
                    "type":"reasoning_required",
                    "source":"decision"
                })

        return {
            "task":task,
            "problems":problems,
            "problem_count":len(problems),
            "needs_improvement":len(problems)>0
        }


problem_detector = ProblemDetector()
