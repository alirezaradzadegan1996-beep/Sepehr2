import json
import os

FILE = "data/projects.json"


class ProjectManager:
    def __init__(self):
        if not os.path.exists(FILE):
            self.save({
                "active_project": None,
                "projects": {}
            })

    def load(self):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # گرفتن پروژه فعال
    def get_active(self):
        data = self.load()
        name = data.get("active_project")

        if not name:
            return None

        project = data["projects"].get(name)

        if not project:
            return None

        return {
            "name": name,
            "step": project.get("step", 1),
            "status": project.get("status", "active")
        }

    # فعال کردن پروژه
    def set_active(self, name):
        data = self.load()

        if name not in data["projects"]:
            data["projects"][name] = {
                "step": 1,
                "status": "active"
            }

        data["active_project"] = name
        self.save(data)

    # رفتن به مرحله بعد
    def next_step(self):
        data = self.load()

        name = data.get("active_project")
        if not name:
            return None

        data["projects"][name]["step"] += 1

        self.save(data)

        return data["projects"][name]["step"]
