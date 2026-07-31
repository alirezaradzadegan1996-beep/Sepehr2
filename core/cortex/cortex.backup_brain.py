from core.kernel import kernel

class Cortex:

    def __init__(self):
        self.version = "3.0"
        self.name = "Sepehr2"

    def boot(self):
        print("[CORTEX] Booting...")

        import core.capabilities.bootstrap

        for service in kernel.services.values():
            if hasattr(service, "initialize"):
                service.initialize()

        print("[CORTEX] Ready")

    def think(self, text):
        print(f"[THINK] {text}")

        router = kernel.get("router")

        if router:
            return router.route(text)

        return "هیچ Router فعالی ثبت نشده است."

cortex = Cortex()
