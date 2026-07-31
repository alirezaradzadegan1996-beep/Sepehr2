import json
import os


class TemplateMemory:

    def __init__(self):

        self.path="data/template_memory.json"

        if not os.path.exists(self.path):
            with open(self.path,"w") as f:
                json.dump({},f)


    def save(self,name,result):

        with open(self.path,"r") as f:
            data=json.load(f)

        data[name]=result

        with open(self.path,"w") as f:
            json.dump(data,f,indent=2)


template_memory=TemplateMemory()
