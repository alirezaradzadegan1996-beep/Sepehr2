from core.cortex.service import Service


class ProjectService(Service):

    name = "ProjectService"

    def __init__(self, planner, skill_engine):
        self.planner = planner
        self.skill_engine = skill_engine


    def handle(self, text):

        plan = self.planner.create_plan(
            text,
            "project"
        )

        result = self.skill_engine.execute(
            plan
        )

        return result
