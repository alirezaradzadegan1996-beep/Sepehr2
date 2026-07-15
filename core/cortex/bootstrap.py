from core.cortex.cortex import cortex
from core.skill_registry import get_skills


def boot():

    print("🧠 Booting Sepehr OS...\n")

    services = {
        "skills": get_skills()
    }


    for name, service in services.items():

        if not cortex.has(name):
            cortex.register(name, service)

        print(f"✅ {name} ready")


    modules = [
        "memory",
        "knowledge",
        "planner",
        "reasoning",
        "decision",
    ]


    for module in modules:
        print(f"✅ {module} ready")


    print("\n🚀 Sepehr OS Ready")

    return cortex
