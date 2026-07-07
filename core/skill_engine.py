from core.skills.app_builder import AppBuilder


class SkillEngine:
    def __init__(self, project_manager):
        self.pm = project_manager

    def execute(self, plan):
        intent = plan.get("intent")
        project = plan.get("project")
        step = plan.get("step")

        print("[SkillEngine] Intent detected:", intent)
        print("[Skill] Project:", project)
        print("[Skill] Step:", step)

        # =========================
        # APP DEVELOPMENT
        # =========================
        if intent == "app_development":
            return AppBuilder.run(project, step)

        # =========================
        # DEFAULT
        # =========================
        return {
            "status": "error",
            "message": "مهارت مناسب برای این درخواست پیدا نشد."
        }
