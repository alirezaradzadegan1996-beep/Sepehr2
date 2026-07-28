from core.capabilities.manager import manager


class SystemCapability:

    name = "system"


    def can_handle(self, text):

        keys = [
            "قابلیت",
            "توانایی",
            "وضعیت سپهر",
            "وضعیت"
        ]

        return any(k in text for k in keys)


    def handle(self, text):

        if "قابلیت" in text or "توانایی" in text:

            return {
                "capabilities": manager.list()
            }


        if "وضعیت" in text:

            return {
                "name": "Sepehr2",
                "version": "3.0",
                "capabilities": manager.info()
            }


        return None


capability = SystemCapability()
