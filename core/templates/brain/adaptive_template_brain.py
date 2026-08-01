from core.templates.template_creator import template_creator
from core.templates.brain.template_memory import template_memory
from core.templates.brain.gap_detector import gap_detector


class AdaptiveTemplateBrain:


    def normalize(self,text):

        words=text.replace(
            "بساز",
            ""
        ).split()

        return "_".join(words[-2:])


    def understand(self,request):

        name=self.normalize(request)

        features=[]

        for w in [
            "فروش",
            "مدیریت",
            "کاربر",
            "دیتابیس",
            "محصول",
            "رزرو",
            "پرداخت",
            "انبار"
        ]:

            if w in request:
                features.append(w)


        if not features:
            features=[
                "database",
                "users",
                "interface"
            ]


        return {
            "name":name,
            "features":features
        }



    def get_template(self,request):

        result=self.understand(request)

        name=result["name"]

        if gap_detector.need_creation(name):

            template_creator.create(
                name,
                result["features"]
            )


        template_memory.remember(
            name,
            result["features"]
        )


        return name



adaptive_template_brain=AdaptiveTemplateBrain()
