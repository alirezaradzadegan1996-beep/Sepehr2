from core.goals.decision import goal_decision
from core.learning.priority_reasoner import priority_reasoner
from core.goals.autonomous_runner import autonomous_goal_runner


class GrowthLoop:


    def run(self, goal):


        analysis = goal_decision.decide(goal)


        ranked = priority_reasoner.rank(
            [
                {
                    "skill": x["need"],
                    "priority": 0
                }
                for x in analysis["missing"]
            ]
        )


        if not ranked:

            return {
                "status":"goal_completed"
            }


        next_skill = ranked[0]


        result = autonomous_goal_runner.run(goal)


        return {

            "goal":goal,

            "next_skill":next_skill,

            "result":result

        }



growth_loop = GrowthLoop()
