class Memory:
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    # 🧠 ساخت پروژه
    def set_project(self, task):
        self.data["project"] = {
            "name": task,
            "history": [task],
            "state": "active"
        }

    # 🧠 آپدیت پروژه
    def update_project(self, text):
        project = self.data.get("project")

        if not project:
            self.set_project(text)
            return

        project["history"].append(text)

        self.data["project"] = project

    # 🧠 گرفتن پروژه
    def get_project(self):
        return self.data.get("project")
