
class AutonomousProjectCreator:

    def create(self, idea):

        return {
            "idea": idea,
            "plan": "generated",
            "code": "generated",
            "test": "generated",
            "status": "PROJECT_CREATED"
        }


autonomous_project_creator = AutonomousProjectCreator()
