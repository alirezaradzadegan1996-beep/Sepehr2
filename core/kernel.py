from core.intent import detect_intent
from core.cortex.system_bus import bus
from core.cortex.cortex import cortex
from core.cortex.system_bus import bus
from core.normalizer import normalize


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
        self.cortex = cortex
        self.router = None

        try:
            self.router = self.cortex.get("router")
        except Exception:
            pass



    def start(self):
        print("[Kernel] Ready")
        bus.publish("kernel.started")



    def process(self, user_input):

        # -------------------------
        # Clean Input
        # -------------------------

        user_input = user_input.replace(
            "[Kernel] Received:",
            ""
        )

        user_input = user_input.replace(
            "kernel received",
            ""
        )

        user_input = user_input.replace(
            "علیرضا:",
            ""
        )

        user_input = user_input.strip()


        print("\n[Kernel] Received:", user_input)


        bus.publish(
            "kernel.input",
            user_input
        )


        # -------------------------
        # Cortex Decision
        # -------------------------

        decision = self.cortex.decide(user_input)

        print(
            "[DECISION]",
            decision.decision.decision_type,
            decision.decision.confidence,
        )

        # -------------------------
        # Search Service
        # -------------------------

        # -------------------------
        # Dispatcher
        # -------------------------

        dispatcher = self.cortex.get("dispatcher")

        result = dispatcher.dispatch(
            decision.decision.service,
            user_input,
        )

        if result is not None:

            if isinstance(result, dict):
                return result.get(
                    "message",
                    str(result),
                )

            return result

        intent = detect_intent(user_input)

        print("[INTENT]", intent)


        bus.publish(
            "intent.detected",
            intent
        )


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




        # ---------- Cortex Router ----------
        if self.router:
            try:
                cortex_answer = self.router.handle(user_input)

                if cortex_answer:
                    return cortex_answer

            except Exception as e:
                print("[CORTEX ROUTER ERROR]", e)




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
