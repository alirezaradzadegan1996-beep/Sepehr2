from core.memory import Memory
from core.planner import Planner
from core.skill_engine import SkillEngine
from core.kernel import Kernel
from core.context_memory import ContextMemory


memory = Memory()
planner = Planner(memory)
skill_engine = SkillEngine(memory)
context_memory = ContextMemory()

kernel = Kernel(memory, planner, skill_engine, context_memory)

kernel.start()

while True:
    user_input = input("\nعلیرضا: ")

    if user_input == "خروج":
        print("سپهر: خداحافظ ❤️")
        break

    result = kernel.process(user_input)

    print("\nسپهر:", result)
