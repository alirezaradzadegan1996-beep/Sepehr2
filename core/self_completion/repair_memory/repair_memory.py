import json
import os

FILE = "data/self_completion/repair_memory.json"


class RepairMemory:

    def __init__(self):
        os.makedirs(
            "data/self_completion",
            exist_ok=True
        )

        if not os.path.exists(FILE):
            with open(FILE,"w",encoding="utf-8") as f:
                json.dump([],f)


    def save(self, experience):

        data = self.all()

        data.append(experience)

        with open(FILE,"w",encoding="utf-8") as f:
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
            with open(FILE,encoding="utf-8") as f:
                return json.load(f)

        except:
            return []


    def search(self, problem):

        results=[]

        for item in self.all():

            if problem.lower() in str(item).lower():
                results.append(item)

        return results



repair_memory = RepairMemory()
