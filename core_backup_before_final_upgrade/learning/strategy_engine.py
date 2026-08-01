from core.memory.experience_memory import experience_memory


class LearningStrategyEngine:


    def analyze(self):


        experiences = experience_memory.recall()


        success = []

        failed = []


        for item in experiences:


            if item.get("result") == "success":

                success.append(
                    item
                )

            else:

                failed.append(
                    item
                )


        strategy = []


        if success:

            strategy.append(
                "successful capabilities should be reused as patterns"
            )


        if failed:

            strategy.append(
                "failed capabilities require improvement"
            )


        return {

            "total_experiences":len(experiences),

            "successful":len(success),

            "failed":len(failed),

            "strategy":strategy

        }



learning_strategy = LearningStrategyEngine()
