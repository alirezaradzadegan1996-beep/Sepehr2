from core.capabilities import registry


class SkillGrowthEngine:


    def analyze_need(self, weakness):

        if weakness.get("weakness") == "missing_capability":

            return {

                "action": "create_capability",

                "reason": weakness["task"],

                "status": "learning_required"

            }


        return {

            "action": "none",

            "status": "no_growth_needed"

        }



    def grow(self, weakness):

        plan = self.analyze_need(weakness)

        return plan



skill_growth = SkillGrowthEngine()
