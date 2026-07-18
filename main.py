from core.memory import Memory
from core.planner import Planner
from core.skill_engine import SkillEngine
from core.kernel import Kernel
from core.context_memory import ContextMemory

from core.cortex.bootstrap import boot
from core.cortex.cortex import cortex


def create_system():

    memory = Memory()

    planner = Planner(memory)

    skill_engine = SkillEngine(
        memory,
        cortex
    )

    # Boot Cortex after dependencies are ready
    boot(
        planner,
        skill_engine
    )


    context_memory = ContextMemory()


    kernel = Kernel(
        memory,
        planner,
        skill_engine,
        context_memory
    )


    # -------------------------
    # Runtime Services
    # -------------------------

    cortex.register_safe(
        "planner",
        planner
    )

    cortex.register_safe(
        "context",
        context_memory
    )

    cortex.register_safe(
        "kernel",
        kernel
    )


    return kernel



kernel = None


def run():

    global kernel

    kernel = create_system()

    kernel.start()


    while True:

        user_input = input("\nعلیرضا: ")


        if user_input.strip() == "خروج":
            print("سپهر: خداحافظ ❤️")
            break


        result = kernel.process(user_input)

        print("\nسپهر:", result)



if __name__ == "__main__":
    run()
