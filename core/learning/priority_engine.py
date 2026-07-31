import json
import os


QUEUE_FILE = "data/learning_queue.json"


class LearningPriorityEngine:


    def __init__(self):

        self.queue = []

        self.load()



    def load(self):

        if os.path.exists(QUEUE_FILE):

            with open(
                QUEUE_FILE,
                encoding="utf-8"
            ) as f:

                self.queue = json.load(f)



    def save(self):

        with open(
            QUEUE_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.queue,
                f,
                ensure_ascii=False,
                indent=2
            )



    def add(self, analysis):


        skill = analysis.get(
            "task",
            "unknown"
        )


        for item in self.queue:

            if item.get("skill") == skill:

                return item



        item = {

            "skill": skill,

            "priority": analysis.get(
                "importance",
                1
            ),

            "status": "waiting"

        }


        self.queue.append(item)

        self.save()


        return item



    def next(self):

        if not self.queue:

            return None


        return max(
            self.queue,
            key=lambda x:x["priority"]
        )



    def list(self):

        return self.queue



learning_priority = LearningPriorityEngine()
