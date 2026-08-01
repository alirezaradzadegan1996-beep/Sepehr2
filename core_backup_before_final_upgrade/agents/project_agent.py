from core.actions.manager import manager
from core.agents.actions.project_actions import create_project_chain


class ProjectAgent:


    name = "project_agent"


    def initialize(self):

        if not manager.get("project_build"):

            create_project_chain(manager)



    def run(self, task):

        chain = manager.get(
            "project_build"
        )

        if chain:

            return chain.run(task)


        return {
            "error": "project build chain not found"
        }



project_agent = ProjectAgent()
