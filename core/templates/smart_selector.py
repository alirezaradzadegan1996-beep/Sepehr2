
import os
import json

class SmartTemplateSelector:

    def __init__(self):
        with open(
        "core/templates/registry/templates.json",
        encoding="utf-8"
        ) as f:
            self.registry=json.load(f)


    def select(self,features):

        for name,data in self.registry.items():

            if any(x in features for x in data):
                return name

        return "general"


smart_selector=SmartTemplateSelector()
