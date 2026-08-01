import os
import json


class TemplateRegistry:

    def __init__(self):
        self.path = "data/templates_registry.json"

        if not os.path.exists(self.path):
            os.makedirs("data", exist_ok=True)
            with open(self.path,"w",encoding="utf-8") as f:
                json.dump({},f,ensure_ascii=False,indent=2)


    def register(self,name,files):

        with open(self.path,"r",encoding="utf-8") as f:
            data=json.load(f)

        data[name]={
            "files":files,
            "usage":0
        }

        with open(self.path,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)


    def get(self,name):

        with open(self.path,"r",encoding="utf-8") as f:
            data=json.load(f)

        return data.get(name)


template_registry=TemplateRegistry()
