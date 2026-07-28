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
            "ایجاد کن",
            "تولید کن"
        ]

        return any(k in text for k in keywords)



    def handle(self, text):


        project_keywords = [
            "اپ",
            "برنامه",
            "پروژه",
            "ماشین حساب",
            "فروشگاه",
            "سایت"
        ]


        if any(k in text for k in project_keywords):

            return {
                "agent": "project_agent",
                "result": project_agent.run(text)
            }



        chain = manager.get("system_task")


        if chain:

            return {
                "agent": "system",
                "result": chain.run(text)
            }


        return {
            "error": "no action chain"
        }



action_service = ActionService()
