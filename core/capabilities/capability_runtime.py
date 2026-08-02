
from core.capabilities.runtime_selector import runtime_selector
from core.capabilities.capability_executor import capability_executor


class CapabilityRuntime:

    def run(self, request):

        selected = runtime_selector.select(
            request
        )

        result = capability_executor.execute(
            selected["capability"]
        )

        return {
            "selection": selected,
            "execution": result,
            "status": "pass"
        }


capability_runtime = CapabilityRuntime()
