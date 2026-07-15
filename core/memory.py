from core.project_manager import ProjectManager


class Memory:
    def __init__(self):
        self.data = {}
        from core.project_manager import ProjectManager

        self.project_manager = ProjectManager()

    # -------------------------
    # Memory
    # -------------------------

    def save(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def clear(self):
        self.data.clear()

    # -------------------------
    # Project Manager
    # -------------------------

    def start_project(self, task):
        return self.project_manager.start_project(task)

    def get_active_project(self):
        return self.project_manager.get_active()

    def set_active_project(self, project):
        return self.project_manager.set_active(project)

    def next_project_step(self):
        return self.project_manager.next_step()

    def save_projects(self):
        return self.project_manager.save()

    def load_projects(self):
        return self.project_manager.load()
