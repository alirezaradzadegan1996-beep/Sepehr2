from datetime import datetime


class ForgettingSystem:


    def __init__(self):

        self.archive = []


    def evaluate(self, memory):

        importance = memory.get(
            "importance",
            0
        )

        confidence = memory.get(
            "confidence",
            0
        )

        access = memory.get(
            "access_count",
            0
        )


        score = (
            importance * 0.5
            +
            confidence * 0.3
            +
            min(access,10) * 0.2
        )


        return round(score,2)



    def should_forget(self, memory):

        score = self.evaluate(memory)

        return score < 2



    def forget(self, memories):

        kept = []
        removed = []


        for item in memories:

            if self.should_forget(item):

                item["forgotten_at"] = str(
                    datetime.now()
                )

                removed.append(item)

                self.archive.append(item)

            else:

                kept.append(item)


        return {

            "status":"forget_complete",

            "kept":kept,

            "removed":removed,

            "archive_count":len(
                self.archive
            )

        }



forgetting_system = ForgettingSystem()
