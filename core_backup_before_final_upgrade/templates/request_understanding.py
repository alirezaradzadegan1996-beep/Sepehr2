
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
