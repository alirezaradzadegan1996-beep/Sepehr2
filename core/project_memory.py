import json
import os
from datetime import datetime


FILE = "data/projects_memory.json"


class ProjectMemory:

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

            except Exception:
                self.memory = []

        else:
            self.memory = []

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

    def remember_project(self, project):

        if not project:
            return None

        # همیشه آخرین نسخه حافظه را بخوان
        self.load()

        analysis = project.get(
            "analysis",
            {}
        )

        reasoning = analysis.get(
            "reasoning",
            {}
        )

        optimization = analysis.get(
            "optimization",
            {}
        )

        test_result = project.get(
            "test_result",
            ""
        )

        test_status = (
            "passed"
            if "✅ تست موفق" in test_result
            else "failed"
        )

        record = {
            "id": project.get("id"),

            "name": project.get(
                "goal",
                "unknown"
            ),

            "type": analysis.get(
                "type",
                "general"
            ),

            "status": project.get(
                "status",
                "completed"
            ),

            "architecture": reasoning.get(
                "architecture",
                []
            ),

            "files": optimization.get(
                "files",
                analysis.get("files", [])
            ),

            "features": analysis.get(
                "features",
                []
            ),

            "suggestions": reasoning.get(
                "suggestions",
                []
            ),

            "evolution": reasoning.get(
                "evolution",
                {}
            ),

            "test_status": test_status,

            "test_result": test_result,

            "date": datetime.now().isoformat(
                timespec="seconds"
            )
        }

        for index, item in enumerate(self.memory):

            if item.get("id") == record["id"]:

                # حفظ اطلاعات یادگیری تجربه
                record["feedback_score"] = item.get(
                    "feedback_score",
                    0
                )

                record["experience_successes"] = item.get(
                    "experience_successes",
                    0
                )

                record["experience_failures"] = item.get(
                    "experience_failures",
                    0
                )

                self.memory[index] = record
                self.save()
                return record

        self.memory.append(record)

        self.save()

        return record

    def get_projects(self):
        return self.memory
