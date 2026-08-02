import json
import os
from datetime import datetime


FILE = "data/self_completion/evolution_memory.json"


class EvolutionMemory:

    def __init__(self):
        os.makedirs(
            "data/self_completion",
            exist_ok=True
        )


    def save(self, experience):

        try:
            with open(FILE, encoding="utf-8") as f:
                data = json.load(f)

        except:
            data = []


        experience["time"] = str(datetime.now())

        data.append(experience)


        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )


        return {
            "status":"saved",
            "experience":experience
        }


    def all(self):

        try:
            with open(FILE, encoding="utf-8") as f:
                return json.load(f)

        except:
            return []


evolution_memory = EvolutionMemory()
