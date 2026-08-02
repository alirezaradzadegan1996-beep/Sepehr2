
from core.evolution.system_analyzer import system_analyzer
from core.evolution.upgrade_planner import upgrade_planner


class SelfDeveloper:

    def improve(self, system):

        analysis = system_analyzer.analyze(
            system
        )

        upgrade = upgrade_planner.plan(
            analysis
        )

        return {
            "analysis": analysis,
            "upgrade": upgrade,
            "status": "SELF_DEVELOPMENT_ACTIVE"
        }


self_developer = SelfDeveloper()
