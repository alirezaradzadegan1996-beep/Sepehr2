from core.services.memory_service import memory_service


class MemoryCapability:

    name = "memory"


    def score(self, text):

        score = 0

        keywords = [
            "یاد بگیر",
            "ذخیره",
            "حافظه",
            "به یاد داشته باش"
        ]

        for k in keywords:

            if k in text:
                score += 10


        return score


    def can_handle(self, text):

        return self.score(text) > 0


    def handle(self, text):

        return memory_service.handle(text)


capability = MemoryCapability()
