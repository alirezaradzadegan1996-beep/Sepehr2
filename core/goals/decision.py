from core.capabilities import registry
from core.capabilities.loader import discover
from core.goals.planner import goal_planner
from core.brain.improved_decision import improved_decision


class GoalDecision:


    def decide(self, goal):


        # sync capabilities
        discover()


        plan = goal_planner.analyze(goal)


        abilities = registry.list()


        missing = []


        for sub in plan["sub_goals"]:

            for need in sub["needs"]:

                if need not in abilities:

                    experience = improved_decision.decide(
                        need
                    )

                    missing.append(
                        {
                            "need": need,
                            "area": sub["name"],
                            "experience": experience
                        }
                    )


        return {

            "goal": goal,

            "current_abilities": abilities,

            "missing": missing

        }



goal_decision = GoalDecision()
