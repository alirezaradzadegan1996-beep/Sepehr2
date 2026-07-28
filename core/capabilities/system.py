from core.capabilities.manager import manager


class SystemCapability:

    name = "system"


    def score(self, text):

        score = 0

        keywords = {
            "قابلیت": 20,
            "توانایی": 20,
            "وضعیت سپهر": 20,
            "وضعیت": 10
        }

        for key, value in keywords.items():

            if key in text:
                score += value

        return score


    def can_handle(self, text):

        return self.score(text) > 0


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
