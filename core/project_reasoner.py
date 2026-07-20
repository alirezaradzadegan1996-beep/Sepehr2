from core.project_experience import ProjectExperience
from core.experience_evolution import ExperienceEvolution
from core.experience_bridge import ExperienceBridge


class ProjectReasoner:

    def __init__(self):
        self.experience = ProjectExperience()
        self.evolution = ExperienceEvolution()
        self.experience_bridge = ExperienceBridge()


    def analyze(self, project):

        if not project:
            return {
                "error": "No project"
            }


        if isinstance(project, str):
            goal = project
        else:
            goal = project.get("goal", "")


        text = goal.lower()


        result = {
            "goal": goal,
            "architecture": [],
            "modules": [],
            "suggestions": []
        }


        if "فروشگاه" in text or "فروش" in text or "shop" in text:

            result["type"] = "ecommerce"

            result["architecture"] = [
                "Product Manager",
                "Shopping Cart",
                "Database Layer",
                "User System"
            ]

            result["modules"] = [
                "main.py",
                "product.py",
                "cart.py",
                "database.py",
                "user.py",
                "test.py"
            ]

            result["suggestions"] = [
                "ذخیره کالاها در دیتابیس",
                "سیستم جستجوی محصولات",
                "مدیریت کاربران",
                "ثبت سفارش"
            ]


        elif "ربات" in text:

            result["type"] = "robot"

            result["architecture"] = [
                "Sensor Layer",
                "Control System",
                "Decision Engine"
            ]

            result["modules"] = [
                "main.py",
                "sensor.py",
                "motor.py",
                "brain.py",
                "test.py"
            ]

            result["suggestions"] = [
                "کالیبراسیون سنسورها",
                "کنترل خطا",
                "ثبت اطلاعات عملکرد"
            ]


        elif "هوش مصنوعی" in text or "ai" in text:

            result["type"] = "ai_agent"

            result["architecture"] = [
                "Brain",
                "Memory",
                "Learning System",
                "Decision Engine"
            ]

            result["modules"] = [
                "main.py",
                "brain.py",
                "memory.py",
                "learner.py",
                "decision.py",
                "test.py"
            ]

            result["suggestions"] = [
                "ذخیره تجربه‌ها",
                "یادگیری از پروژه‌های قبلی",
                "تحلیل تصمیم‌ها"
            ]


        elif "ماشین حساب" in text or "calculator" in text:

            result["type"] = "calculator"

            result["architecture"] = [
                "Calculation Engine",
                "Input Handler"
            ]

            result["modules"] = [
                "main.py",
                "calculator.py",
                "test.py"
            ]

            result["suggestions"] = [
                "اضافه کردن عملیات بیشتر",
                "مدیریت خطا",
                "رابط کاربری"
            ]


        elif "دما" in text or "temperature" in text:

            result["type"] = "temperature_converter"

            result["architecture"] = [
                "Converter Engine",
                "Input Handler"
            ]

            result["modules"] = [
                "main.py",
                "temperature.py",
                "test.py"
            ]

            result["suggestions"] = [
                "اضافه کردن واحدهای بیشتر",
                "رابط کاربری بهتر"
            ]


        elif (
            "روزشمار" in text
            or "تقویم" in text
            or "calendar" in text
            or "یادآوری" in text
            or "یادآور" in text
        ):

            result["type"] = "calendar_app"

            result["architecture"] = [
                "Calendar Engine",
                "Reminder System",
                "Storage Layer"
            ]

            result["modules"] = [
                "main.py",
                "calendar.py",
                "reminder.py",
                "database.py",
                "test.py"
            ]

            result["suggestions"] = [
                "ثبت رویدادها",
                "نمایش تاریخ",
                "ذخیره یادآوری‌ها"
            ]



        # گرفتن تجربه قبلی
        experience = self.experience.get_experience(
            result["type"],
            goal
        )


        result["experience"] = experience
        result["experience_used"] = False
        result["reasoning_source"] = "base_reasoning"


        if experience.get("found"):

            confidence = experience.get(
                "confidence",
                "low"
            )

            result["experience_confidence"] = confidence


            if confidence == "high":

                result["architecture"] = list(dict.fromkeys(
                    result["architecture"]
                    +
                    experience.get("architecture", [])
                ))


                result["modules"] = list(dict.fromkeys(
                    result["modules"]
                    +
                    experience.get("files", [])
                ))


                result["suggestions"] = list(dict.fromkeys(
                    result["suggestions"]
                    +
                    experience.get("features", [])
                    +
                    experience.get("suggestions", [])
                ))


                result["experience_used"] = True

                result["reasoning_source"] = (
                    "base_reasoning+trusted_project_experience"
                )


                evolution = self.evolution.evolve(
                    goal,
                    result,
                    experience
                )


                result["evolution"] = evolution


                if evolution.get("evolved"):

                    result["modules"] = evolution.get(
                        "modules",
                        result["modules"]
                    )

                    result["suggestions"] = evolution.get(
                        "suggestions",
                        result["suggestions"]
                    )


                    result["experience_evolved"] = True

                    result["reasoning_source"] += (
                        "+experience_evolution"
                    )


            elif confidence == "medium":

                result["suggestions"] = list(dict.fromkeys(
                    result["suggestions"]
                    +
                    experience.get("features", [])
                    +
                    experience.get("suggestions", [])
                ))

                result["experience_used"] = True


                result["reasoning_source"] = (
                    "base_reasoning+suggested_project_experience"
                )


            else:

                result["reasoning_source"] = (
                    "base_reasoning+observed_project_experience"
                )


        # اتصال حافظه تجربه جدید
        result = self.experience_bridge.enrich_reasoning(
            result.get("type", "general"),
            result
        )


        return result
