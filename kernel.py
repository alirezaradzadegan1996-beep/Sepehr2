from core.brain.router import Router
from core.planner import Planner


class Kernel:
    def __init__(self, memory, planner, skill_engine, context_memory):
        self.memory = memory
        self.router = Router()
        self.planner = planner
        self.skill_engine = skill_engine
        self.context_memory = context_memory

        self.pm = self.memory.project_manager

        self.state = "INIT"

    def start(self):
        self.state = "RUNNING"
        print("[Kernel] System Started")

    def process(self, user_input):
        print("\n[Kernel] Received:", user_input)

        user_input = user_input.strip()

        route = self.router.route(user_input)

        if route["type"] == "system":
            print("[System]", route["response"])
            return route["response"]

        user_input = route["data"]

        # -------------------------
        # ادامه پروژه
        # -------------------------
        if user_input in ["بعدی", "ادامه", "ادامه بده"]:

            project = self.memory.get_active_project()

            if project is None:
                return "❌ هیچ پروژه فعالی وجود ندارد."

            self.memory.next_project_step()

            project = self.memory.get_active_project()

            plan = self.planner.create_plan(project["task"])
            plan["step"] = project["step"]
            plan["project"] = project

        else:

            plan = self.planner.create_plan(user_input)

        result = self.skill_engine.execute(plan)

        self.memory.save("last_input", user_input)
        self.memory.save("last_plan", plan)
        self.memory.save("last_result", result)

        return result
