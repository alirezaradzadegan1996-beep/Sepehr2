from core.memory import Memory
from core.planner import Planner

memory = Memory()

planner = Planner(memory)

task = "برام یک اپ حسابداری بساز"

plan = planner.create_plan(task)

print("\nPLAN:")
print(plan)
