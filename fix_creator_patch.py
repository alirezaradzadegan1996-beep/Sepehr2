import os

os.makedirs("core/self_completion/evolution", exist_ok=True)

code = '''
from core.capabilities.base.capability import Capability


class DebuggerCapability(Capability):

    name = "debugger"

    keywords = [
        "debugger",
        "debug",
        "خطا",
        "اشکال"
    ]

    def run(self, text):
        return {
            "status": "active",
            "capability": "debugger"
        }


capability = DebuggerCapability()
'''

with open(
    "core/capabilities/debugger.py",
    "w",
    encoding="utf-8"
) as f:
    f.write(code)


print("[✓] debugger capability file created")


from core.capabilities.registry import registry

try:
    from core.capabilities.debugger import capability
    registry.register("debugger", capability)
    print("[✓] debugger registered")
except Exception as e:
    print("REGISTER ERROR:", e)


print("CAPABILITIES:")
print(registry.list())
