from core.project_manager import ProjectManager


class Planner:


    def __init__(self, memory):

        self.memory = memory
        self.pm = self.memory.project_manager



    def create_plan(self, task, intent=None):

        print("[Planner] Understanding task...")


        project = self.memory.get_active_project()


        # اگر Intent از قبل آمده استفاده کن
        if intent is None:

            intent = self.detect_intent(task)



        if project is None:

            return {

                "task": task,

                "project": None,

                "intent": intent,

                "step": 0,

                "status": "planned"

            }



        return {

            "task": task,

            "project": self.pm.active,

            "intent": intent,

            "step": project.get(
                "step",
                0
            ),

            "status": project.get(
                "status",
                "active"
            )

        }



    def detect_intent(self, task):

        task = task.lower()


        if "اپ" in task or "برنامه" in task:

            return "app_development"


        if "ریاضی" in task or "محاسبه" in task:

            return "calculation"


        return "general"
