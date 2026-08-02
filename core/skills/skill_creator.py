
from core.skills.skill_registry import skill_registry

class SkillCreator:

    def create(self,name):
        skill={
            "name":name,
            "version":1,
            "status":"created"
        }

        skill_registry.register(
            name,
            skill
        )

        return skill

skill_creator=SkillCreator()
