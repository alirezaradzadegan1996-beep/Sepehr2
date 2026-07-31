import json
import os
from datetime import datetime


FILE = "data/improvement_memory.json"


class ImprovementMemory:


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



    def add(self, action, result):

        item = {

            "time": str(datetime.now()),

            "action": action,

            "result": result

        }


        self.data.append(item)

        self.save()


        return item



    def recall(self):

        return self.data



    def find(self, action):

        return [
            x for x in self.data
            if x.get("action") == action
        ]



improvement_memory = ImprovementMemory()
