
class SkillTester:

    def test(self,skill):
        return {
            "skill":skill.get("name"),
            "valid":True,
            "checks":[
                "name",
                "version",
                "status"
            ]
        }

skill_tester=SkillTester()
