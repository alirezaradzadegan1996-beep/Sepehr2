from core.knowledge import search_knowledge
from core.cortex.service import Service


class KnowledgeService(Service):

    name = "knowledge"

    def search(self, text):
        return search_knowledge(text)

    def handle(self, text):
        return self.search(text)
