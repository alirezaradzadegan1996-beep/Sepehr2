import json
import os
from datetime import datetime


FILE = "data/strategy_memory.json"


class StrategyMemory:


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



    def add(self, action, status, confidence):

        item = {

            "time": str(datetime.now()),

            "action": action,

            "status": status,

            "confidence": confidence

        }


        self.data.append(item)

        self.save()

        return item



    def recall(self):

        return self.data



    def preferred(self):

        return [
            x for x in self.data
            if x.get("status") == "preferred"
        ]



strategy_memory = StrategyMemory()
