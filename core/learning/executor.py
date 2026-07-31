from core.learning.skill_growth import skill_growth
from core.learning.capability_creator import capability_creator


class LearningExecutor:


    def execute(self, item):


        if item is None:

            return {
                "status": "empty_learning_queue"
            }


        skill = item.get(
            "skill"
        )


        weakness = {

            "task": skill,

            "weakness": "missing_capability"

        }


        plan = skill_growth.grow(
            weakness
        )


        if plan["action"] == "create_capability":


            result = capability_creator.create(
                skill
            )


            return {

                "skill": skill,

                "plan": plan,

                "creation": result

            }



        return {

            "skill": skill,

            "status": "no_action"

        }



learning_executor = LearningExecutor()
