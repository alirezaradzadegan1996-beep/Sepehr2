
class UpgradePlanner:

    def plan(self, analysis):

        return {
            "analysis": analysis,
            "upgrade": "generated",
            "status": "planned"
        }


upgrade_planner = UpgradePlanner()
