from core.cortex.service import Service
from core.planner import Planner


class PlannerService(Service):

    name = "planner"

    def __init__(self):
        self.planner = None

    def initialize(self, memory):
        self.planner = Planner(memory)

    def create_plan(self, task, intent=None):
        if self.planner:
            return self.planner.create_plan(
                task,
                intent,
            )

        return None

    def handle(self, text):
        return self.create_plan(text)
