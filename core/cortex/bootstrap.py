from core.cortex.cortex import Cortex

cortex = Cortex()


def boot():

    print("🧠 Booting Sepehr OS...\n")

    modules = [
        "memory",
        "knowledge",
        "planner",
        "reasoning",
        "skills",
        "decision"
    ]

    for module in modules:
        cortex.register(module, module)
        print(f"✅ {module} loaded")

    print("\n🚀 Sepehr OS Ready")

    return cortex
