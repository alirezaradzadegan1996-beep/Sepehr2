from core.actions.manager import manager
from core.agents.actions.system_actions import create_system_chain
from core.agents.project_agent import project_agent


class ActionService:


    def initialize(self):

        if not manager.get("system_task"):
            create_system_chain(manager)

        project_agent.initialize()



    def boot(self):

        print("[Action] Ready")



    def can_handle(self, text):

        keywords = [
            "بساز",
            "ساخت",
            "ایجاد",
            "تولید",
            "طراحی",
            "پیاده سازی",
            "درست کن",
            "انجام بده"
        ]

        return any(k in text for k in keywords)



    def handle(self, text):

        # تمام درخواست‌های ساخت به ProjectAgent می‌روند
        return {
            "agent": "project_agent",
            "result": project_agent.run(text)
        }



action_service = ActionService()
