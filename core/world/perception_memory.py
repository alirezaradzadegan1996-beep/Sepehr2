
import json
import os

FILE="data/world_memory.json"


class PerceptionMemory:

    def save(self, data):

        os.makedirs(
            "data",
            exist_ok=True
        )

        try:
            with open(FILE,encoding="utf-8") as f:
                memory=json.load(f)
        except:
            memory=[]

        memory.append(data)

        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                memory,
                f,
                ensure_ascii=False,
                indent=2
            )

        return {
            "status":"saved"
        }


    def all(self):

        try:
            with open(FILE,encoding="utf-8") as f:
                return json.load(f)
        except:
            return []


perception_memory=PerceptionMemory()
