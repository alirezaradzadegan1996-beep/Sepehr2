from core.brain.router import Router
from core.planner import Planner


class Kernel:
    def __init__(self, memory, planner, skill_engine, context_memory):
        self.memory = memory
        self.router = Router()
        self.planner = planner
        self.skill_engine = skill_engine
        self.context_memory = context_memory

        # 🔥 Project Manager (خیلی مهم برای قفل پروژه)
        self.pm = self.memory.project_manager

        self.state = "INIT"

    def start(self):
        self.state = "RUNNING"
        print("[Kernel] System Started")

    def process(self, user_input):
        print("\n[Kernel] Received:", user_input)

        user_input = user_input.strip()

        route = self.router.route(user_input)

        # اگر system command بود
        if route["type"] == "system":
            print("[System]", route["response"])
            return route["response"]

        # اگر task بود ادامه بده
        user_input = route["data"]

        # =========================
        # 🔥 STEP COMMAND (بعدی)
        # =========================
        if user_input == "بعدی":
            print("[Kernel] STEP COMMAND DETECTED")

            project = self.pm.get_active()

            if not project:
                return "❌ هیچ پروژه فعالی وجود ندارد"

            # رفتن به مرحله بعد
            step = self.pm.next_step()

            # ساخت پلن بر اساس پروژه فعال
            plan = self.planner.create_plan(project["name"])
            plan["step"] = step

        else:
            # حالت عادی
            plan = self.planner.create_plan(user_input)

        # =========================
        # اجرای Skill Engine
        # =========================
        result = self.skill_engine.execute(plan)

        # =========================
        # ذخیره وضعیت
        # =========================
        self.memory.save("last_input", user_input)
        self.memory.save("last_plan", str(plan))
        self.memory.save("last_result", str(result))

        return result
