from core.learning.priority_engine import learning_priority


class LearningStateManager:


    def update(self, skill, status):

        for item in learning_priority.queue:

            if item.get("skill") == skill:

                item["status"] = status

        learning_priority.save()


        return {
            "skill": skill,
            "status": status
        }



    def complete(self, skill):

        return self.update(
            skill,
            "completed"
        )



state_manager = LearningStateManager()
