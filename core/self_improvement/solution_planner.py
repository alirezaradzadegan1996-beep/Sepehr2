class SolutionPlanner:

    def plan(self, detection):

        plans = []

        for problem in detection.get("problems", []):

            p = problem.get("type")

            if p == "low_confidence":
                plans.append({
                    "problem":p,
                    "solution":"improve_reasoning_quality"
                })

            elif p == "no_success_history":
                plans.append({
                    "problem":p,
                    "solution":"create_experience_pattern"
                })

            elif p == "learning_needed":
                plans.append({
                    "problem":p,
                    "solution":"expand_knowledge"
                })

            elif p == "reasoning_required":
                plans.append({
                    "problem":p,
                    "solution":"upgrade_reasoning_engine"
                })

        return {
            "status":"plan_created",
            "plans":plans,
            "count":len(plans)
        }


solution_planner = SolutionPlanner()
