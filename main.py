from core.memory import Memory
from core.planner import Planner
from core.skill_engine import SkillEngine
from core.kernel import Kernel
from core.context_memory import ContextMemory

from core.cortex.bootstrap import boot
from core.cortex.cortex import cortex
from core.cortex.skill_manager import SkillManager
from core.skill_registry import get_skills


# Boot Sepehr OS
boot()


# Create core services
memory = Memory()
planner = Planner(memory)
skill_engine = SkillEngine(memory, cortex)
from core.skill_registry import get_skills

cortex.set_skills(
    get_skills()
)
context_memory = ContextMemory()

kernel = Kernel(memory, planner, skill_engine, context_memory)


# Register services in Cortex
cortex.register("memory", memory)
cortex.register("planner", planner)
cortex.register("context", context_memory)
cortex.register("kernel", kernel)


# Start Kernel
kernel.start()


# Main Loop
while True:
    user_input = input("\nعلیرضا: ")

    if user_input == "خروج":
        print("سپهر: خداحافظ ❤️")
        break

    result = kernel.process(user_input)

    print("\nسپهر:", result)
