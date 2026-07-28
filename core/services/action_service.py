from core.actions.manager import manager
from core.agents.actions.system_actions import create_system_chain


class ActionService:


    def initialize(self):

        if not manager.get("system_task"):
            create_system_chain(manager)


    def boot(self):

        print("[Action] Ready")


    def can_handle(self, text):

        keywords = [
            "بساز",
            "ساخت",
            "ایجاد کن"
        ]

        return any(k in text for k in keywords)


    def handle(self, text):

        chain = manager.get("system_task")

        if chain:

            return chain.run(text)

        return {
            "error": "chain missing"
        }


action_service = ActionService()
