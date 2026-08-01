import os
import shutil
from datetime import datetime

print("""
====================================
SEPEHR2 PRIORITY RANKING UPGRADE
====================================
""")

target = "core/decision/decision_core.py"

backup = target + ".backup_priority_ranking"

if os.path.exists(target):
    shutil.copy2(target, backup)
    print("[✓] Backup created:", backup)


with open(target, encoding="utf-8") as f:
    code = f.read()


if "capability_priority_memory" not in code:

    code = code.replace(
        "from core.brain.improved_decision import improved_decision",
        """from core.brain.improved_decision import improved_decision
from core.memory.capability_priority_memory import capability_priority_memory"""
    )


old = """
existing = registry.route(text)

if existing:
"""

new = """
existing_candidates = []

try:
    candidates = registry.find_candidates(text)

    for item in candidates:
        name = item.get("name")

        priority = capability_priority_memory.get(name)

        bonus = priority.get(
            "priority",
            0
        ) / 100

        item["score"] = (
            item.get("score",0)
            +
            bonus
        )

    candidates.sort(
        key=lambda x:x.get("score",0),
        reverse=True
    )

    if candidates:
        existing = candidates[0]["name"]
    else:
        existing = registry.route(text)

except Exception:
    existing = registry.route(text)


if existing:
"""


if old in code:
    code = code.replace(old,new)
else:
    print("[!] Existing block not found - skipping")


with open(target,"w",encoding="utf-8") as f:
    f.write(code)


print("[✓] Priority ranking patch completed")


# TEST

from core.decision.decision_core import decision_core

print("""
========== TEST ==========
""")

print(
    decision_core.decide(
        "برای من یک اپ مدیریت گلخانه بساز"
    )
)


print("""
====================================
PRIORITY RANKING COMPLETE
====================================
""")

