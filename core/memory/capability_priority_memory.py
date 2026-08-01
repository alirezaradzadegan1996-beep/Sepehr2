import json
import os
from datetime import datetime


FILE = "data/capability_scores.json"


class CapabilityPriorityMemory:

    def __init__(self):
        self.data = {}
        self.load()


    def load(self):

        if os.path.exists(FILE):

            with open(
                FILE,
                encoding="utf-8"
            ) as f:

                self.data = json.load(f)

        else:

            self.data = {}


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


    def update(
        self,
        capability,
        score
    ):

        self.data[capability] = {

            "score": score,

            "priority": int(
                score * 100
            ),

            "updated":
                str(datetime.now())
        }

        self.save()


        return {
            "status":"updated",
            "capability":capability,
            "score":score,
            "priority":
                int(score*100)
        }


    def get(self, capability):

        return self.data.get(
            capability,
            {
                "score":0,
                "priority":0
            }
        )


    def all(self):

        return self.data



capability_priority_memory = CapabilityPriorityMemory()
