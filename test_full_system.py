from core.memory import Memory
from core.planner import Planner
from core.skill_engine import SkillEngine


# حافظه
memory = Memory()

# پلنر
planner = Planner(memory)

# اسکیل انجین
engine = SkillEngine(memory)

# درخواست کاربر
task = "برام یک اپ ماشین حساب بساز"

# 1. برنامه‌ریزی
plan = planner.create_plan(task)

print("\n📌 PLAN:")
print(plan)

# 2. اجرا
result = engine.execute(plan)

print("\n🚀 RESULT:")
print(result)
