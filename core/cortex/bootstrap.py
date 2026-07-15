from core.cortex.cortex import cortex
from core.skill_registry import get_skills


def boot():

    print("🧠 Booting Sepehr OS...\n")


    # Load skills into Cortex SkillManager

    skills = get_skills()

    cortex.set_skills(
        skills
    )


    print("✅ skills ready")


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
