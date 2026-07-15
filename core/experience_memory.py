import json
import os
from collections import Counter


FILE = "data/experience_memory.json"


class ExperienceMemory:

    def __init__(self):
        self.load()


    def load(self):

        if os.path.exists(FILE):

            try:
                with open(
                    FILE,
                    "r",
                    encoding="utf-8"
                ) as f:
                    self.memory = json.load(f)

                    if not isinstance(self.memory, dict):
                        self.memory = {}

            except Exception:
                self.memory = {}

        else:
            self.memory = {}


    def save(self):

        os.makedirs(
            "data",
            exist_ok=True
        )

        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.memory,
                f,
                ensure_ascii=False,
                indent=4
            )


    def learn_from_project(self, project):

        if not project:
            return {
                "learned": False
            }


        project_type = project.get(
            "type",
            "general"
        )


        if project_type not in self.memory:

            self.memory[project_type] = {

                "success_count": 0,
                "features": [],
                "files": [],
                "suggestions": []

            }


        exp = self.memory[project_type]


        test_passed = False


        if project.get("test_status") == "passed":
            test_passed = True


        if "✅ تست موفق" in project.get(
            "test_result",
            ""
        ):
            test_passed = True


        if project.get("success") is True:
            test_passed = True


        if test_passed:
            exp["success_count"] += 1


        for feature in project.get(
            "evolution_features",
            []
        ):

            if feature not in exp["features"]:
                exp["features"].append(feature)


        for file in project.get(
            "files",
            []
        ):

            if file not in exp["files"]:
                exp["files"].append(file)


        for suggestion in project.get(
            "suggestions",
            []
        ):

            if suggestion not in exp["suggestions"]:
                exp["suggestions"].append(
                    suggestion
                )


        self.save()


        return {
            "learned": True,
            "type": project_type,
            "success_count": exp["success_count"]
        }



    def get_best_practices(self, project_type):

        if project_type not in self.memory:
            return {
                "found": False
            }


        data = self.memory[project_type]

        success = data.get(
            "success_count",
            0
        )


        if success >= 3:
            confidence = "high"

        elif success >= 2:
            confidence = "medium"

        else:
            confidence = "low"


        return {
            "found": True,
            "type": project_type,
            "confidence": confidence,
            "success_count": success,
            "features": data.get(
                "features",
                []
            ),
            "files": data.get(
                "files",
                []
            ),
            "suggestions": data.get(
                "suggestions",
                []
            )
        }
