import os
import shutil
from datetime import datetime

print("""
====================================
 SEPEHR2 MEMORY INTELLIGENCE UPGRADE
====================================
""")

FILES = [
    "core/decision/decision_core.py",
    "core/runtime/runtime_router_bridge.py",
    "core/memory/consolidation_engine.py",
    "core/memory/capability_priority_memory.py"
]


# =========================
# BACKUP
# =========================

backup_dir = "backup_memory_upgrade_" + datetime.now().strftime("%Y%m%d_%H%M%S")

os.makedirs(backup_dir, exist_ok=True)

for f in FILES:
    if os.path.exists(f):
        shutil.copy2(
            f,
            os.path.join(
                backup_dir,
                os.path.basename(f)
            )
        )

print("[✓] Backup created:", backup_dir)


# =========================
# VERIFY MODULES
# =========================

checks = [
    ("Consolidated Memory",
     "data/consolidated_memory.json"),

    ("Capability Scores",
     "data/capability_scores.json"),

    ("Experiences",
     "data/experiences.json")
]


for name,path in checks:

    if os.path.exists(path):
        print("[✓]", name, "available")

    else:
        print("[!]", name, "missing")


# =========================
# VERIFY DECISION
# =========================

try:

    from core.decision.decision_core import decision_core

    result = decision_core.decide(
        "برای من یک اپ مدیریت گلخانه بساز"
    )

    print("\nDecision Test:")
    print(result)

except Exception as e:

    print("Decision Error:",e)



# =========================
# VERIFY MEMORY
# =========================

try:

    from core.memory.consolidation_engine import consolidation_engine

    result = consolidation_engine.consolidate()

    print("\nMemory Consolidation:")
    print(
        result.get("status")
    )

except Exception as e:

    print("Memory Error:",e)



# =========================
# VERIFY CAPABILITY
# =========================

try:

    from core.capabilities.registry import registry

    print("\nCapability Route:")

    print(
        registry.route(
            "برای من یک اپ مدیریت گلخانه بساز"
        )
    )

except Exception as e:

    print("Capability Error:",e)



print("""
====================================
 UPGRADE CHECK COMPLETE
====================================
""")
