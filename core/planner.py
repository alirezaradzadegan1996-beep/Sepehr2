from core.project_manager import ProjectManager


class Planner:
    def __init__(self, memory):
        self.memory = memory
        self.pm = ProjectManager()

    def create_plan(self, task):
        print("[Planner] Understanding task...")

        self.memory.update_project(task)

        project = self.memory.get_project()

        if not project:
            return {
                "task": task,
                "project": None,
                "intent": self.detect_intent(task),
                "step": 1,
                "status": "planned"
            }

        project_name = project["name"]

        task = self.resolve_context(task, project)

        intent = self.detect_intent(task)

        step = self.pm.get_step()

        plan = {
            "task": task,
            "project": project_name,
            "step": step,
            "intent": intent,
            "status": project.get("status", "active")
        }

        self.memory.save("last_plan", str(plan))
        return plan

    def resolve_context(self, task, project):
        task_lower = task.lower()

        follow_words = ["بعدی", "ادامه", "توضیح بده", "اولیش", "دومیش"]

        if any(word in task_lower for word in follow_words):
            print("[Planner] STEP MODE ACTIVE")

            self.pm.next_step()

            step = self.pm.get_step()

            print(f"[Planner] Current Step: {step}")

            return f"{project['name']} | step_{step}"

        return task

    def detect_intent(self, task):
        task = task.lower()

        if "اپ" in task or "برنامه" in task:
            return "app_development"

        if "ریاضی" in task or "محاسبه" in task:
            return "calculation"

        return "general"
