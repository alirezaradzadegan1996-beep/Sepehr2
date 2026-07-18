"""
Sepehr2 Cortex Health Service
بررسی سلامت سرویس‌ها
"""


class HealthService:

    name = "health"


    def __init__(self, cortex):
        self.cortex = cortex


    def check(self):

        services = [
            "memory",
            "knowledge",
            "reasoning",
            "context",
            "router",
            "planner",
        ]

        result = [
            "🧠 Sepehr Cortex Status\n"
        ]

        for service in services:

            try:
                obj = self.cortex.get(service)

                if obj:
                    result.append(
                        f"{service:<12} ✅ online"
                    )

            except Exception:
                result.append(
                    f"{service:<12} ❌ offline"
                )


        return "\n".join(result)
