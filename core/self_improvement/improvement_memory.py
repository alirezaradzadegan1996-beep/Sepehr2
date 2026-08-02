import json
import os
from datetime import datetime


class ImprovementMemory:

    def __init__(self):
        self.file = "data/improvement_history.json"

        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.file):
            with open(self.file,"w",encoding="utf-8") as f:
                json.dump([],f,ensure_ascii=False)


    def save(self, record):

        with open(self.file,"r",encoding="utf-8") as f:
            data=json.load(f)

        record["time"]=str(datetime.now())

        data.append(record)

        with open(self.file,"w",encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False
            )

        return {
            "status":"saved",
            "count":len(data)
        }


    def get_history(self):

        with open(self.file,"r",encoding="utf-8") as f:
            return json.load(f)


improvement_memory = ImprovementMemory()
