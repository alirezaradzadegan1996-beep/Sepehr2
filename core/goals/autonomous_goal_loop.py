from core.goals.goal_generator import goal_generator
from core.goals.goal_priority import goal_priority
from core.learning.autonomous_executor import autonomous_executor
from core.brain.self_model_updater import self_model_updater


class AutonomousGoalLoop:


    def run(self):

        goals = goal_generator.generate()


        selected = goal_priority.select(
            goals
        )


        if not selected:

            return {
                "status":"no_goal"
            }


        goal = selected["selected"]


        skill = goal["skill"]


        execution = autonomous_executor.run(
            skill
        )


        update = self_model_updater.update(
            skill
        )


        return {

            "goal": goal,

            "execution": execution,

            "self_update": update

        }



autonomous_goal_loop = AutonomousGoalLoop()
