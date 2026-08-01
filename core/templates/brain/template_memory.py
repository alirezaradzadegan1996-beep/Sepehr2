import os
import json


class TemplateMemory:

    def __init__(self):
        self.path="data/templates/template_memory.json"

        os.makedirs(
            "data/templates",
            exist_ok=True
        )

        if not os.path.exists(self.path):
            with open(self.path,"w",encoding="utf-8") as f:
                json.dump({},f)


    def load(self):

        with open(
            self.path,
            encoding="utf-8"
        ) as f:
            return json.load(f)


    def save(self,data):

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


    def remember(self,name,features):

        data=self.load()

        data[name]={
            "features":features,
            "usage":data.get(name,{}).get("usage",0)+1
        }

        self.save(data)


template_memory=TemplateMemory()
