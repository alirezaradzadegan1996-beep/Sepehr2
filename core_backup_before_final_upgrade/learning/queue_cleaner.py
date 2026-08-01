from core.learning.priority_engine import learning_priority


class QueueCleaner:


    def clean(self):

        unique = {}

        for item in learning_priority.queue:

            skill = item.get("skill")


            if skill not in unique:

                unique[skill] = item

            else:

                # نگه داشتن اولویت بالاتر
                if item.get("priority",0) > unique[skill].get("priority",0):

                    unique[skill] = item



        learning_priority.queue = list(
            unique.values()
        )

        learning_priority.save()


        return learning_priority.queue



queue_cleaner = QueueCleaner()
