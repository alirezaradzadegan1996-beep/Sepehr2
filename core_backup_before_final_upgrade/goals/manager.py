import json
import os


FILE = "data/goals.json"


class GoalManager:


    def __init__(self):

        self.goals = []

        self.load()



    def load(self):

        if os.path.exists(FILE):

            with open(
                FILE,
                encoding="utf-8"
            ) as f:

                self.goals = json.load(f)



    def save(self):

        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.goals,
                f,
                ensure_ascii=False,
                indent=2
            )



    def add(self, goal):

        self.goals.append(
            {
                "goal": goal,
                "status": "active"
            }
        )

        self.save()


        return self.goals[-1]



    def list(self):

        return self.goals



goal_manager = GoalManager()
