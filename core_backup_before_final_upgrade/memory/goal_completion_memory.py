import json
import os
from datetime import datetime


FILE = "data/goal_completion.json"


class GoalCompletionMemory:


    def __init__(self):

        self.data = []

        self.load()



    def load(self):

        if os.path.exists(FILE):

            with open(
                FILE,
                encoding="utf-8"
            ) as f:

                self.data = json.load(f)



    def save(self):

        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.data,
                f,
                ensure_ascii=False,
                indent=2
            )



    def add(self, goal, skill):

        record = {

            "time": str(datetime.now()),

            "goal": goal,

            "skill": skill,

            "status":"completed"

        }


        self.data.append(record)

        self.save()

        return record



    def exists(self, skill):

        for item in self.data:

            if item.get("skill") == skill:

                return True


        return False



    def recall(self):

        return self.data



goal_completion_memory = GoalCompletionMemory()
