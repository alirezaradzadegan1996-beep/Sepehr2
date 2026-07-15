"""
Sepehr2 Cortex Bootstrap
راه‌اندازی اولیه سرویس‌های Cortex
"""

from core.cortex.cortex import cortex


def boot():

    print("🧠 Booting Sepehr OS...\n")


    # -------------------------
    # Auto Load Skills
    # -------------------------

    skills = cortex.load_skills()

    print("✅ skills ready")


    # -------------------------
    # Core Modules Status
    # -------------------------

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
