from core.goals.re_evaluator import goal_re_evaluator
from core.learning.autonomous_executor import autonomous_executor


class GrowthController:


    def run(self, goal):


        evaluation = goal_re_evaluator.evaluate(
            goal
        )


        if evaluation["status"] == "completed":

            return {
                "status":"goal_completed",
                "goal":goal
            }


        skill = evaluation["next_need"]["need"]


        result = autonomous_executor.run_once()


        return {

            "goal":goal,

            "selected_skill":skill,

            "evaluation":evaluation,

            "execution":result

        }



growth_controller = GrowthController()
