from core.reasoning_engine import reason
from core.cortex.service import Service


class ReasoningService(Service):

    name = "reasoning"

    def think(self, text):
        return reason(text)

    def handle(self, text):
        return self.think(text)
