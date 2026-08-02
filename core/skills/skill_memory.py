
import json
import os


FILE="data/skill_memory.json"


class SkillMemory:

    def save(self,data):

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

        with open(FILE,"w",encoding="utf-8") as f:
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


skill_memory=SkillMemory()
