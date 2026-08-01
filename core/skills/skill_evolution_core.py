from datetime import datetime

try:
    from core.capabilities.registry import registry
except:
    registry = None


class SkillEvolutionCore:

    def __init__(self):
        self.skills = {}


    def has_skill(self, name):
        return name in self.skills


    def create_skill(self, name, purpose):

        if self.has_skill(name):
            return {
                "status": "already_exists",
                "skill": name
            }

        self.skills[name] = {
            "name": name,
            "purpose": purpose,
            "version": "1.0",
            "created": str(datetime.now())
        }

        if registry:
            registry.register(
                name,
                self.skills[name]
            )

        return {
            "status": "created",
            "skill": name
        }


    def upgrade_skill(self, name):

        if not self.has_skill(name):
            return {
                "status": "missing",
                "skill": name
            }

        current = float(self.skills[name]["version"])
        current += 0.1
        self.skills[name]["version"] = f"{current:.1f}"

        return {
            "status": "upgraded",
            "skill": name,
            "version": self.skills[name]["version"]
        }


    def auto_prepare(self, request):

        r = request.lower()

        if "ماشین حساب" in r:
            return self.create_skill(
                "calculator_builder",
                "build calculator applications"
            )

        if "فروش خودرو" in r:
            return self.create_skill(
                "car_market_builder",
                "build vehicle marketplace applications"
            )

        return {
            "status": "no_new_skill_needed"
        }


core = SkillEvolutionCore()


if __name__ == "__main__":

    print(core.auto_prepare("یک اپ ماشین حساب بساز"))

    print(core.upgrade_skill("calculator_builder"))

    print({
        "skills": list(core.skills.keys()),
        "count": len(core.skills),
        "status": "skill_evolution_active"
    })
