from datetime import datetime

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)

from core.runtime.runtime_router_bridge import RuntimeRouterBridge


class MainRuntimeBridgeTest:


    def __init__(self):

        self.router = RuntimeRouterBridge()



    def process(self, text):

        result = self.router.execute(text)

        return {
            "input": text,
            "runtime": "main.py",
            "router_result": result,
            "status":"processed"
        }



system = MainRuntimeBridgeTest()


tests = [
    "سلام سپهر",
    "من علیرضا هستم",
    "یک اپ ماشین حساب بساز"
]


for item in tests:
    print(system.process(item))


print(
    {
        "time":str(datetime.now()),
        "status":"main_runtime_bridge_ready"
    }
)

