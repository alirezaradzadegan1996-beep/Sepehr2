
from core.skills.skill_registry import skill_registry

class SkillManager:

    def install(self,name,skill):
        return skill_registry.register(name,skill)

    def list(self):
        return skill_registry.all()

skill_manager=SkillManager()
