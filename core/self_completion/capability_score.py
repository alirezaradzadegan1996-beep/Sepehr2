
import json
import os

FILE="data/self_completion/capability_scores.json"

class CapabilityScore:

    def update(self,name,success=True):

        try:
            data=json.load(open(FILE,encoding="utf-8"))
        except:
            data={}

        item=data.get(name,{
            "success":0,
            "failure":0
        })

        if success:
            item["success"]+=1
        else:
            item["failure"]+=1

        data[name]=item

        json.dump(
            data,
            open(FILE,"w",encoding="utf-8"),
            ensure_ascii=False,
            indent=2
        )

        return item

capability_score=CapabilityScore()
