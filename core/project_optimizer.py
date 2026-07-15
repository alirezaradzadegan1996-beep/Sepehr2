import os


class ProjectOptimizer:


    def optimize(self, analysis):

        print("\n========== PROJECT OPTIMIZER ==========")
        print("[OPTIMIZER] analysis =", analysis)
        print("[OPTIMIZER] detected type =", analysis.get("type"))
        print("=======================================\n")


        project_type = analysis.get(
            "type",
            "general"
        )


        plan = {
            "folders": [],
            "files": [],
            "dependencies": [],
            "database": None,
            "testing": True,
            "quality": [
                "README",
                "UTF-8"
            ]
        }


        if project_type == "ecommerce":

            plan["folders"] = [
                "data",
                "tests"
            ]

            plan["files"] = [
                "main.py",
                "product.py",
                "cart.py",
                "database.py",
                "user.py",
                "test.py",
                "requirements.txt"
            ]

            plan["database"] = "sqlite"


        elif project_type == "calculator":

            plan["files"] = [
                "main.py",
                "calculator.py",
                "test.py"
            ]


        elif project_type == "temperature_converter":

            plan["files"] = [
                "main.py",
                "temperature.py",
                "test.py"
            ]


        else:

            plan["files"] = [
                "main.py",
                "test.py"
            ]


        print("=======================================\n")


        # اعمال تجربه و دانش پروژه‌های قبلی روی Build Plan

        learned_files = analysis.get(
            "learned_files",
            []
        )

        knowledge = analysis.get(
            "knowledge",
            {}
        )

        if learned_files:

            plan["files"] = list(dict.fromkeys(
                plan["files"] + learned_files
            ))

            plan["experience_applied"] = True
            plan["experience_files"] = learned_files

        else:

            plan["experience_applied"] = False
            plan["experience_files"] = []


        if knowledge.get("used"):

            plan["knowledge_applied"] = True

        else:

            plan["knowledge_applied"] = False


        # اعمال Evolution روی Build Plan
        reasoning = analysis.get(
            "reasoning",
            {}
        )

        evolution = reasoning.get(
            "evolution",
            {}
        )

        improvements = evolution.get(
            "improvements",
            []
        )

        evolution_files = []

        for improvement in improvements:

            if "تاریخچه محاسبات" in improvement:
                evolution_files.append("history.py")

            elif "اعتبارسنجی ورودی" in improvement:
                evolution_files.append("validator.py")

            elif "مدیریت تقسیم بر صفر" in improvement:
                evolution_files.append("errors.py")

            elif "ساختار قابل توسعه" in improvement:
                evolution_files.append("operations.py")

        if evolution_files:
            plan["files"] = list(dict.fromkeys(
                plan["files"] + evolution_files
            ))

            plan["evolution_applied"] = True
            plan["evolution_files"] = evolution_files

        else:
            plan["evolution_applied"] = False
            plan["evolution_files"] = []

        print("[OPTIMIZER] build plan =", plan)

        return plan



    def analyze_quality(self, project_path):

        result = {
            "project": project_path,
            "files": [],
            "problems": [],
            "suggestions": []
        }


        if not os.path.exists(project_path):
            result["problems"].append(
                "Project path not found"
            )
            return result


        for root, dirs, files in os.walk(project_path):

            for file in files:

                if file.endswith(".py"):

                    path = os.path.join(
                        root,
                        file
                    )

                    result["files"].append(file)


                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        code = f.read()


                    if len(code.strip()) == 0:

                        result["problems"].append(
                            f"{file} is empty"
                        )


                    if "print(" in code:

                        result["suggestions"].append(
                            f"{file}: replace print with logger"
                        )


        if not result["problems"]:

            result["suggestions"].append(
                "Code structure is acceptable"
            )


        return result
