class ExperienceEvolution:

    def evolve(self, goal, reasoning, experience):

        result = {
            "evolved": False,
            "source_project_id": None,
            "goal": goal,
            "architecture": [],
            "modules": [],
            "suggestions": [],
            "improvements": []
        }

        if not experience.get("found"):
            return result

        if experience.get("confidence") != "high":
            return result

        result["source_project_id"] = experience.get(
            "best_project_id"
        )

        result["architecture"] = list(dict.fromkeys(
            reasoning.get("architecture", [])
            + experience.get("architecture", [])
        ))

        result["modules"] = list(dict.fromkeys(
            reasoning.get("modules", [])
            + experience.get("files", [])
        ))

        result["suggestions"] = list(dict.fromkeys(
            reasoning.get("suggestions", [])
            + experience.get("features", [])
            + experience.get("suggestions", [])
        ))

        project_type = reasoning.get(
            "type",
            "general"
        )

        improvements = []

        if project_type == "calculator":
            improvements = [
                "افزودن تاریخچه محاسبات",
                "اعتبارسنجی ورودی‌ها",
                "مدیریت تقسیم بر صفر",
                "ساختار قابل توسعه برای عملیات جدید"
            ]

        elif project_type == "ecommerce":
            improvements = [
                "مدیریت موجودی کالا",
                "اعتبارسنجی سفارش",
                "ثبت تاریخچه سفارش‌ها",
                "تفکیک لایه منطق و دیتابیس"
            ]

        elif project_type == "ai_agent":
            improvements = [
                "ثبت تصمیم‌های قبلی",
                "امتیازدهی به تجربه‌ها",
                "مدیریت خطای تصمیم",
                "تحلیل نتیجه عملکرد"
            ]

        elif project_type == "robot":
            improvements = [
                "سیستم توقف امن",
                "ثبت داده سنسورها",
                "تشخیص خطای سنسور",
                "کنترل پایدارتر موتور"
            ]

        else:
            improvements = [
                "بهبود مدیریت خطا",
                "افزایش تست‌ها",
                "ساختار ماژولارتر"
            ]

        result["improvements"] = improvements

        result["suggestions"] = list(dict.fromkeys(
            result["suggestions"]
            + improvements
        ))

        result["evolved"] = True

        return result
