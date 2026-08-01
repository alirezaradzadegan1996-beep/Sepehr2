import json
from pathlib import Path

CAP_FILE = Path("data/capabilities.json")


class CapabilityRegistry:

    def __init__(self):
        self.capabilities = {}
        self.load()


    def register(self, name, capability):
        self.capabilities[name] = capability
        self.save()

        return {
            "status": "registered",
            "capability": name
        }


    def find(self, name):
        return self.capabilities.get(name)


    def list(self):
        return list(self.capabilities.keys())


    def route(self, text):
        for name, cap in self.capabilities.items():
            try:
                if cap.can_handle(text):
                    return name
            except:
                pass

        return None


    def save(self):
        CAP_FILE.parent.mkdir(exist_ok=True)

        data = {}

        for name, cap in self.capabilities.items():
            data[name] = {
                "name": name,
                "type": str(type(cap))
            }

        CAP_FILE.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )


    def load(self):
        if CAP_FILE.exists():
            try:
                data = json.loads(
                    CAP_FILE.read_text(encoding="utf-8")
                )

                # فعلاً فقط اطلاعات ثبت‌شده را می‌خوانیم
                # اتصال آبجکت‌ها در مرحله بعد انجام می‌شود

            except Exception:
                pass


# Global Registry Instance
capability_registry = CapabilityRegistry()
