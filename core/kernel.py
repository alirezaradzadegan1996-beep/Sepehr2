from core.intent import detect_intent
from core.cortex.system_bus import bus


class Kernel:

    def __init__(
        self,
        memory,
        planner,
        skill_engine,
        context_memory=None
    ):

        print("[Kernel] System Started")

        self.memory = memory
        self.planner = planner
        self.skill_engine = skill_engine
        self.context_memory = context_memory



    def start(self):
        print("[Kernel] Ready")
        bus.publish("kernel.started")



    def process(self, user_input):

        print("\n[Kernel] Received:", user_input)

        bus.publish("kernel.input", user_input)

        intent = detect_intent(user_input)

        print("[INTENT]", intent)

        bus.publish("intent.detected", intent)


        # خروج

        if user_input.strip() in [
            "خروج",
            "exit",
            "quit"
        ]:

            return "خداحافظ ❤️"



        # سیستم پروژه

        if intent == "project":


            # رفتن به مرحله بعد

            if user_input.strip() == "بعدی":


                result = self.memory.next_project_step()



                # اگر پروژه تمام شده

                if result is None:


                    project = self.memory.get_active_project()



                    if project and project.get("status") == "completed":


                        return (
                            "🚀 پروژه کامل شد.\n\n"
                            f"📌 نام پروژه:\n"
                            f"{project.get('goal')}\n\n"
                            "✅ تحویل پروژه انجام شد."
                        )



                    return "❌ مرحله بعدی وجود ندارد."



                if isinstance(result, dict):

                    return result.get(
                        "message",
                        str(result)
                    )


                bus.publish("kernel.response", result)
                return result




            # ساخت پروژه جدید


            plan = self.planner.create_plan(
                user_input,
                intent
            )


            result = self.skill_engine.execute(
                plan
            )


            if isinstance(result, dict):

                return result.get(
                    "message",
                    str(result)
                )


            bus.publish("kernel.response", result)
            return result




        # درخواست‌های معمولی


        plan = self.planner.create_plan(
            user_input,
            intent
        )


        result = self.skill_engine.execute(
            plan
        )



        if isinstance(result, dict):

            return result.get(
                "message",
                str(result)
            )



        bus.publish("kernel.response", result)
        return result
