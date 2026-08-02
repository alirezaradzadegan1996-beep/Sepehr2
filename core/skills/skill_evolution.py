
class SkillEvolution:

    def upgrade(self,skill):

        skill["version"] += 1
        skill["status"]="evolved"

        return skill


skill_evolution=SkillEvolution()
