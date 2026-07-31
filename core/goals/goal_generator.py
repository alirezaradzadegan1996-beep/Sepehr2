from core.goals.goal_observer import goal_observer


class GoalGenerator:


    def generate(self):

        state = goal_observer.observe()

        goals = []


        for item in state["missing"]:

            goals.append(
                {
                    "goal":f"develop_{item}",
                    "skill":item,
                    "reason":"missing capability",
                    "priority":8
                }
            )


        return goals



goal_generator = GoalGenerator()
