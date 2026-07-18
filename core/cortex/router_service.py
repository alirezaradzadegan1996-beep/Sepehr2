from core.cortex.service import Service


class RouterService(Service):

    name = "router"


    def __init__(self, cortex):
        self.cortex = cortex


    def handle(self, text):

        text = text.strip()


        # -------------------------
        # Greeting
        # -------------------------

        greetings = [
            "سلام",
            "درود",
            "سلام سپهر",
            "خوبی"
        ]

        if any(
            g in text
            for g in greetings
        ):
            return "سلام علیرضا ❤️ خوشحالم که دوباره با هم روی Sepehr2 کار می‌کنیم."


        # -------------------------
        # Memory
        # -------------------------

        if "من کی هستم" in text:

            memory = self.cortex.get(
                "memory"
            )

            if memory:
                return memory.summary()



        # -------------------------
        # Knowledge
        # -------------------------

        knowledge = self.cortex.get(
            "knowledge"
        )

        if knowledge:

            answer = knowledge.search(
                text
            )

            if answer:
                return answer



        # -------------------------
        # Reasoning
        # -------------------------

        reasoning = self.cortex.get(
            "reasoning"
        )

        if reasoning:

            if hasattr(
                reasoning,
                "handle"
            ):
                result = reasoning.handle(
                    text
                )

                if result:
                    return result


            if hasattr(
                reasoning,
                "reason"
            ):
                result = reasoning.reason(
                    text
                )

                if result:
                    return result



        return "هنوز پاسخ مناسبی پیدا نکردم."
