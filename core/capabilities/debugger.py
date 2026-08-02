
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
