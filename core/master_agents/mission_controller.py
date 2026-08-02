

class MissionController:

    def execute(self,mission):

        return {
            "mission":mission,
            "planning":"completed",
            "execution":"active",
            "status":
            "AUTONOMOUS_MISSION_CONTROLLER_ACTIVE"
        }


mission_controller=MissionController()

