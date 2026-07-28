from core.services.action_service import action_service


class ActionCapability:

    name = "action"


    def score(self, text):

        score = 0

        keywords = [
            "بساز",
            "ساخت",
            "ایجاد کن",
            "درست کن",
            "تولید کن"
        ]

        for k in keywords:

            if k in text:
                score += 20

        return score


    def can_handle(self, text):

        return self.score(text) > 0


    def handle(self, text):

        return action_service.handle(text)


capability = ActionCapability()
