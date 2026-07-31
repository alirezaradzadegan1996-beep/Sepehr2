import os
import json


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        f.write(content)


# 1 Request Understanding
write(
"core/templates/request_understanding.py",
'''
import re

class RequestUnderstanding:

    def analyze(self,text):

        t=text.lower()

        project="general"
        features=["database","users","interface"]

        rules={
            "ماشین حساب":"calculator",
            "فروشگاه":"ecommerce",
            "بیمارستان":"hospital",
            "مزرعه":"farm",
            "گلخانه":"greenhouse",
            "رستوران":"restaurant",
            "خودرو":"car_marketplace",
            "عکس":"image_editor",
            "ادیت":"image_editor"
        }

        for k,v in rules.items():
            if k in t:
                project=v

        if project=="ecommerce":
            features += [
                "products",
                "cart",
                "inventory"
            ]

        if project=="hospital":
            features += [
                "patients",
                "doctors",
                "appointments"
            ]

        if project=="image_editor":
            features += [
                "upload",
                "filters",
                "resize",
                "save"
            ]

        return {
            "project_type":project,
            "features":features
        }


request_understanding=RequestUnderstanding()
'''
)


# 2 Feature Brain
write(
"core/templates/feature_brain.py",
'''
class FeatureBrain:

    def extract(self,project):

        return {
            "core_features":project.get("features",[]),
            "generated":True
        }


feature_brain=FeatureBrain()
'''
)


# 3 Template Memory
write(
"data/template_memory.json",
json.dumps({},indent=4)
)


# 4 Adaptive Template Manager
write(
"core/templates/adaptive_template_manager.py",
'''
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
'''
)


# 5 Universal Template Engine
write(
"core/templates/template_engine.py",
'''
import os


class TemplateEngine:


    def load(self,result):

        files={}

        if isinstance(result,dict):

            path=result.get("path")

            if not path:

                path=f"core/templates/generated/{result.get('template')}"


        else:

            path=f"core/templates/generated/{result}"


        if not os.path.exists(path):
            return files


        for f in os.listdir(path):

            with open(
                os.path.join(path,f),
                encoding="utf-8"
            ) as x:

                files[
                    f.replace(".template","")
                ]=x.read()


        return files



template_engine=TemplateEngine()
'''
)


# 6 Builder Intelligence Connection
path="core/builder/full_builder_engine.py"

if os.path.exists(path):

    data=open(path,encoding="utf-8").read()

    data=data.replace(
"template_engine.load(\n            template\n        )",
"template_engine.load(template)"
)

    data=data.replace(
"template = adaptive_template_manager.get_template(\n            intent[\"project_type\"],\n            intent[\"features\"]\n        )",
"template = adaptive_template_manager.get_template(\n            intent[\"project_type\"],\n            intent[\"features\"]\n        )"
)

    open(path,"w",encoding="utf-8").write(data)



# 7 Project Knowledge
write(
"data/projects_brain.json",
json.dumps(
{
"examples":{
"hospital":[
"patients",
"doctors",
"appointments"
],
"image_editor":[
"upload",
"filters",
"resize"
]
}
},
indent=4,
ensure_ascii=False
)
)



# 8 Test
write(
"core/templates/template_intelligence_test.py",
'''
from core.templates.request_understanding import request_understanding
from core.templates.adaptive_template_manager import adaptive_template_manager


tests=[
"یک اپ بیمارستان بساز",
"یک اپ ادیت عکس بساز",
"یک فروشگاه اینترنتی بساز"
]


for t in tests:

    intent=request_understanding.analyze(t)

    print(t)
    print(intent)

    print(
    adaptive_template_manager.get_template(
        intent["project_type"],
        intent["features"]
    ))
'''
)


print("Template Intelligence Upgrade Completed")
