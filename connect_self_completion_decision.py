import os

path="core/decision/decision_core.py"

print("CHECKING:", path)

if os.path.exists(path):
    print("[✓] Decision Core Found")
else:
    print("[X] Missing Decision Core")
