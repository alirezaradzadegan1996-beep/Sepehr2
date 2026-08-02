
import json
from pathlib import Path

FILE="data/session_memory.json"

class SessionMemory:

    def save(self,data):
        Path("data").mkdir(exist_ok=True)

        try:
            with open(FILE,encoding="utf-8") as f:
                memory=json.load(f)
        except:
            memory=[]

        memory.append(data)

        with open(FILE,"w",encoding="utf-8") as f:
            json.dump(memory,f,ensure_ascii=False,indent=2)

        return {
            "status":"saved",
            "data":data
        }


    def all(self):
        try:
            with open(FILE,encoding="utf-8") as f:
                return json.load(f)
        except:
            return []


session_memory=SessionMemory()
