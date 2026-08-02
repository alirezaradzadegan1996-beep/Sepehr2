
from core.skills.skill_registry import skill_registry

class SkillBootstrap:

    def load(self):
        return {
            "status":"loaded",
            "skills":skill_registry.all()
        }

skill_bootstrap=SkillBootstrap()
