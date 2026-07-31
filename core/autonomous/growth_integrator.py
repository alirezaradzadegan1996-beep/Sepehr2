from core.brain.self_model_updater import self_model_updater
from core.goals.re_evaluator import goal_re_evaluator
from core.learning.priority_reasoner import priority_reasoner
from core.learning.autonomous_executor import autonomous_executor


class GrowthIntegrator:


    def run_cycle(self, goal):


        # بررسی وضعیت فعلی هدف

        evaluation = goal_re_evaluator.evaluate(
            goal
        )


        if evaluation["status"] == "completed":

            return {

                "status":"completed",

                "goal":goal

            }



        skill = evaluation["next_need"]["need"]


        # اجرای یادگیری قابلیت

        result = autonomous_executor.run(skill)



        # ثبت در مدل خود

        self_model_updater.update(
            skill
        )



        # بررسی دوباره

        next_state = goal_re_evaluator.evaluate(
            goal
        )


        return {

            "goal":goal,

            "completed_skill":skill,

            "execution":result,

            "next_state":next_state

        }



growth_integrator = GrowthIntegrator()
