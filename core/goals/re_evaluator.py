from core.goals.decision import goal_decision
from core.brain.self_map import self_map


class GoalReEvaluator:


    def evaluate(self, goal):


        current = self_map.status()


        decision = goal_decision.decide(
            goal
        )


        missing = decision.get(
            "missing",
            []
        )


        completed = current.get(
            "completed",
            []
        )


        remaining = []


        for item in missing:

            skill = item.get(
                "need"
            )

            if skill not in completed:

                remaining.append(
                    item
                )


        if remaining:


            next_skill = remaining[0]


            return {

                "goal":goal,

                "status":"in_progress",

                "completed":completed,

                "next_need":next_skill

            }


        return {

            "goal":goal,

            "status":"completed",

            "completed":completed

        }



goal_re_evaluator = GoalReEvaluator()
