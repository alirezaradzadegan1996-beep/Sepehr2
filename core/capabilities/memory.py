from core.services.memory_service import memory_service


class MemoryCapability:

    name = "memory"

    def can_handle(self, text):

        keywords = [
            "یاد بگیر",
            "ذخیره",
            "حافظه",
            "به یاد داشته باش"
        ]

        return any(k in text for k in keywords)


    def handle(self, text):

        return memory_service.handle(text)


capability = MemoryCapability()
