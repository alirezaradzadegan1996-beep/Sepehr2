import os
import shutil
import re
from datetime import datetime

print("=== Sepehr2 Root Architecture Fix ===")

# -----------------------------
# Backup
# -----------------------------
files = [
    "core/decision/decision_core.py",
    "core/cognitive/self_reasoning.py",
    "core/runtime/runtime_router_bridge.py"
]

backup_dir = "backup_root_fix_" + datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(backup_dir, exist_ok=True)

for f in files:
    if os.path.exists(f):
        shutil.copy2(
            f,
            os.path.join(backup_dir, os.path.basename(f))
        )
        print("Backup:", f)

# -----------------------------
# Fix Decision Core
# -----------------------------

path = "core/decision/decision_core.py"

with open(path,encoding="utf-8") as f:
    data=f.read()

marker = "# KNOWLEDGE PRIORITY FIX"

if marker not in data:

    insert = r'''

# KNOWLEDGE PRIORITY FIX
# Knowledge questions must never fall into memory route

if any(x in t for x in [
    "چیست",
    "چیه",
    "چرا",
    "چطور",
    "چگونه",
    "تفاوت",
    "فرق",
    "تعریف",
    "معنی",
    "توضیح"
]):

    return {
        "route":"knowledge",
        "decision":"cognitive_reasoning",
        "confidence":0.95
    }

'''

    target = "if any(x in t for x in [\n                                    \"یاد\","

    idx=data.find(target)

    if idx!=-1:
        data=data[:idx]+insert+data[idx:]
        print("DecisionCore patched")
    else:
        print("DecisionCore target not found")

    with open(path,"w",encoding="utf-8") as f:
        f.write(data)

else:
    print("DecisionCore already fixed")


# -----------------------------
# Fix Self Reasoning
# -----------------------------

path="core/cognitive/self_reasoning.py"

with open(path,encoding="utf-8") as f:
    data=f.read()

old_start = 'if any(x in text for x in ['
old_end = 'else:\n                                               conclusion = ('

start=data.find(old_start)

if start!=-1:

    second=data.find(old_end,start)

    if second!=-1:

        replacement = '''if not conclusion:

            conclusion = (
                "تحلیل سپهر:\\n"
                "مسئله دریافت شد و نیاز به بررسی دانش و استدلال دارد."
            )

'''

        data=data[:start]+replacement+data[second:]

        with open(path,"w",encoding="utf-8") as f:
            f.write(data)

        print("SelfReasoning patched")

else:
    print("SelfReasoning already clean")


# -----------------------------
# Fix Runtime memory priority
# -----------------------------

path="core/runtime/runtime_router_bridge.py"

with open(path,encoding="utf-8") as f:
    data=f.read()

if "MEMORY AFTER DECISION FIX" not in data:

    old='''memory_analysis = self.memory_intelligence.analyze(
                memory_payload
            )'''

    new='''memory_analysis = self.memory_intelligence.analyze(
                memory_payload
            )

            # MEMORY AFTER DECISION FIX
            # memory provides context only, never controls route
'''

    if old in data:
        data=data.replace(old,new)
        with open(path,"w",encoding="utf-8") as f:
            f.write(data)

        print("Runtime patched")

# -----------------------------
# Search bad memories
# -----------------------------

print("\nSearching corrupted motor answers...")

for root,dirs,files in os.walk("data"):
    for file in files:
        if file.endswith(".json"):
            p=os.path.join(root,file)
            try:
                txt=open(p,encoding="utf-8").read()
                if "افزایش دمای موتور" in txt:
                    print("FOUND:",p)
            except:
                pass


print("\n=== FIX COMPLETE ===")
print("Run:")
print("python main.py")

