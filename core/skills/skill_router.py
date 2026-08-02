
from core.skills.skill_registry import skill_registry

class SkillRouter:

    def route(self,text):
        for name in skill_registry.all():
            if name.lower() in text.lower():
                return skill_registry.get(name)

        return None

skill_router=SkillRouter()
