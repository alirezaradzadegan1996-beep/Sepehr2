
class GoalGenerator:

    def generate(self, need):

        return {
            "goal": need,
            "status": "created"
        }


goal_generator_upgrade = GoalGenerator()
