
import os
import json

from core.templates.template_creator import template_creator


class AdaptiveTemplateManager:


    def __init__(self):

        self.memory="data/template_memory.json"


    def get_template(self,name,features):

        path=f"core/templates/generated/{name}"

        if os.path.exists(path):

            return {
                "template":name,
                "status":"exists"
            }


        result=template_creator.create(
            name,
            features
        )


        return result



adaptive_template_manager=AdaptiveTemplateManager()
